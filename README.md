## Projeto Final - Implementação do operador linear para o crosstalk eletrônico.
----

### Introdução:
De _Crosstalk Identification in xDSL Systems_, desprezando o ruído, o sinal observado no _i_-ésimo canal pode ser descrito pelo seguinte diagrama de blocos:

<p align="center">
<img width="416" height="161" alt="image" src="https://github.com/user-attachments/assets/9b13e25b-32d9-4253-b32f-7a2276913176" />
<p>
onde cada $\underline f_j$ é o sinal ideal (sinal sem crosstalk que cada canal deveria exibir), $N_e$ é o número de canais e $\underline h_{i,j}$ é a resposta ao impulso que representa o crosstalk observado em $\underline g_i$ causado por $\underline f_j$. Desse modo, para um certo sinal observado em $\underline g_i$, temos que:

$$
\begin{align}
\underline g_i = \sum_{j = 1}^{N_e} \underline h_{i, j} * \underline f_j.
\end{align}
$$

Ou seja, para a remoção do crosstalk é de extrema importância conseguirmos escrever o nosso problema no formato $\underline H f = g$ e simplesmente resolver um problema least-squares (ou suas variantes) para descobrirmos qual seria a matriz de sinais ideais $[\underline f_i]\_{i = 1}^{Ne}$ dada a matriz de sinais observados 
$[\underline g_i]\_{i = 1}^{Ne}$.

Entretanto, assumindo que cada $h_{i, j}$ é finita, dependendo do tamanho da matriz de convolução $\underline H$, alocá-la na memória pode ser custoso. Portanto, é interessante desenvolvermos um operador linear do tipo _scipy.LinearOperator_, no qual a funcionalidade é a mesma quando comparada a matriz de convolução, mas o processo é descrito por um funcional linear, ou seja, no lugar de alocarmos uma matriz, é feito chamadas de funções.

----

Colab que demonstra a conversão da matriz de convolução para um operador linear:
----
https://colab.research.google.com/drive/1Mf2YAiU24RBWifKqfNX-F-UKyaxXM3zN?usp=sharing


Implementação do operador linear:
----

Com isso, já que 

$$
\begin{align}
\underline g_i = \sum_{j = 1}^{N_e} \underline h_{i, j} * \underline f_j = \sum_{j = 1}^{N_e} \underline H_{i, j} \underline f_j.
\end{align}
$$

se para cada $i, j \in \\{1, \dots, N_e\\}$, foi possível criar um operador linear $Op_{i, j}$ para representar $\underline H_{i, j}$ (ver colab acima), então,

$$
\begin{align}
\underline g_i = \sum_{j = 1}^{N_e} \underline H_{i, j} \underline f_j \equiv \sum_{j = 1}^{N_e} Op_{i, j}(\underline f_j),
\end{align}
$$

enquanto a adjunta da operação acima pode ser descrita em termos da adjunta de $Op_{i, j}$ da seguinte forma:

$$
\begin{align}
\underline f_i = \sum_{j = 1}^{N_e} \underline H^H_{i, j} \underline g_j \equiv \sum_{j = 1}^{N_e} Op^H_{i, j}(\underline g_j).
\end{align}
$$

obs: no código fornecido não é feito explicitamente a chamada descrita acima, porém,
é possível verificar que a abordagem é equivalente a um caso específico do que foi discutido, onde $m$ e $n$ são iguais.

Colab com demonstração do operador linear aplicado na remoção do crosstalk:
https://colab.research.google.com/drive/1m7mHPk5V4tD1p8f4cMzr6mGot37MFG4M?usp=drive_link
