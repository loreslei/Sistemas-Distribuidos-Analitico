

# Dedução
Para deduzir a disponibilidade de um serviço replicado, tratamos o estado de cada servidor como um evento de Bernoulli independente, onde a probabilidade de sucesso (servidor estar "up") é p.

$$
P(X = i) = \binom{n}{i} p^i (1 - p)^{n-i}
$$

A disponibilidade total A é a soma das probabilidades de todos os sucessos aceitáveis

$$
A = \sum_{i=k}^{n} \binom{n}{i} p^i (1 - p)^{n-i}
$$

# Cálculo analítico




Link do colab https://colab.research.google.com/drive/1jtvLWZfpQGBm_bP6jKyxE_Gqk_XUQnKs?usp=sharing
