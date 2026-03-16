# Equipe

| Nome                                | Matrícula             |
|-------------------------------------|-----------------------|
| Bianca Oriá Leite                   | 2320323               |
| João Felipe Ribeiro de Melo         | 2315045               |
| João Pedro Ribeiro Mendes           | 2315069               |
| Lorenna Aguiar Nunes                | 2315026               |

# Fórmula
## Dedução da Disponibilidade de um Serviço Replicado

Considere:

- **n**: número total de servidores  
- **k**: número mínimo de servidores disponíveis para o serviço funcionar  
- **p**: probabilidade de um servidor estar disponível  

Assumimos que os servidores são **independentes** e possuem a **mesma probabilidade de disponibilidade**.

---

### Probabilidade de exatamente *i* servidores disponíveis

Escolher **i servidores disponíveis entre n** pode ser feito de

$$
\binom{n}{i}
$$

formas.

A probabilidade de exatamente **i servidores estarem disponíveis** e **n−i falharem** é:

$$
P(X = i) = \binom{n}{i} p^i (1 - p)^{n-i}
$$

---

### Disponibilidade do sistema

O sistema funciona quando **pelo menos k servidores estão disponíveis**, ou seja:

$$
X \ge k
$$

Logo, a disponibilidade total é a soma das probabilidades de todos os casos válidos:

$$
A = \sum_{i=k}^{n} \binom{n}{i} p^i (1 - p)^{n-i}
$$

---

### Casos extremos

**Consulta (k = 1)** — basta um servidor disponível:

$$
A = 1 - (1 - p)^n
$$

**Atualização (k = n)** — todos os servidores precisam estar disponíveis:

$$
A = p^n
$$

# Conclusões


# Link do Colab

 https://colab.research.google.com/drive/1jtvLWZfpQGBm_bP6jKyxE_Gqk_XUQnKs?usp=sharing
