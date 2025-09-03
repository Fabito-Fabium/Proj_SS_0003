import matplotlib.pyplot as plt
import numpy as np
import time

import scipy.optimize as so
import scipy.signal as ss
import scipy.sparse.linalg as la

def crs_FIR_linOp(all_h, Nt, Ne):
    total_size = Nt * Ne
    h_len = all_h.shape[0]

    valid_idx = []
    for j in range(Ne):
        for k in range(j, Ne):
            #if j != k:
            valid_idx.append((j, k))

    def matvec(x):
        F = x.reshape(Nt, Ne)
        G = np.zeros_like(F)
        # G recebe F (identidade)
        #G[:, :] = F[:, :]
        for j, k in valid_idx:
            G[:, j] += ss.convolve(F[:, k], all_h[:, j, k], mode='full')[:-(h_len - 1)]
            if j != k:
                G[:, k] += ss.convolve(F[:, j], all_h[:, k, j], mode='full')[:-(h_len - 1)]
        return G.ravel()

    def rmatvec(y):
        G = y.reshape(Nt, Ne)
        F = np.zeros_like(G)
        # F recebe G (identidade)
        #F += G
        for j, k in valid_idx:
            G_padded = np.pad(G[:, j], (0, h_len-1))
            F[:, k] += ss.correlate(G_padded, all_h[:, j, k], mode='valid')

            if j != k:
                G_padded = np.pad(G[:, k], (0, h_len - 1))
                F[:, j] += ss.correlate(G_padded, all_h[:, k, j], mode='valid')

        return F.ravel()

    return la.LinearOperator(shape=(total_size, total_size), matvec=matvec, rmatvec=rmatvec, dtype=np.float64)
