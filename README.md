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

A análise dos gráficos e tabelas permitiu observar como a disponibilidade de um serviço replicado depende diretamente dos parâmetros: número de servidores, número mínimo de servidores necessários e probabilidade de cada servidor estar disponível. A partir da dedução matemática baseada na distribuição binomial, foi possível calcular analiticamente a probabilidade de o sistema permanecer operacional, isto é, de haver pelo menos k servidores disponíveis entre os n existentes. Os resultados mostraram que, à medida que p aumenta, a disponibilidade do sistema cresce, enquanto valores maiores de k tornam o sistema mais restritivo, reduzindo sua disponibilidade.

Os gráficos também evidenciam o impacto do número de servidores dependendo da estratégia adotada. No caso k = 1 (operações de consulta), aumentar o número de servidores melhora significativamente a disponibilidade, pois basta que um servidor esteja ativo. Já no caso k = n (operações de atualização), a disponibilidade tende a diminuir conforme o número de servidores cresce, pois todos precisam estar disponíveis simultaneamente. O caso intermediário, como k ≈ n/2, representa um equilíbrio entre disponibilidade e consistência, demonstrando o trade-off típico de sistemas distribuídos. Além disso, o Gráfico 4 analisa quantos servidores são necessários para atingir diferentes níveis de disponibilidade alvo — 90%, 99%, 99.9%, 99.99%, 99.999% e 99.9999% — mostrando que, conforme se busca níveis cada vez mais altos de confiabilidade (os chamados “nove de disponibilidade”), é necessário aumentar significativamente o número de servidores, evidenciando que alcançar alta disponibilidade possui custo crescente em infraestrutura.

Por fim, o simulador estocástico confirmou os resultados obtidos pela fórmula analítica. Ao executar um grande número de rodadas aleatórias para diferentes valores de n, k e p, a frequência experimental de disponibilidade se aproximou dos valores teóricos calculados pela fórmula. Essa convergência entre simulação e modelo matemático demonstra que a abordagem probabilística utilizada descreve adequadamente o comportamento do sistema e permite prever como diferentes configurações de replicação afetam a disponibilidade do serviço.


# Link do Colab

 https://colab.research.google.com/drive/1jtvLWZfpQGBm_bP6jKyxE_Gqk_XUQnKs?usp=sharing
