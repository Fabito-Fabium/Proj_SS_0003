## Projeto Final - Implementação do operador linear para o crosstalk.


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

Para realizar a transição entre operador linear e matriz de convolução, teremos que explorar a relação entre matrizes de convolução e a operação convolução.

### Relação entre matriz de convolução e convolução para sinais discretos:
