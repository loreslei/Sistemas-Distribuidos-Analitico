import math
import matplotlib.pyplot as plt
import numpy as np

def disponibilidade_analitica(n, k, p):
    disponibilidade = 0.0
    for i in range(k, n + 1):
        combinacao = math.comb(n, i)
        probabilidade_i = combinacao * (p ** i) * ((1 - p) ** (n - i))
        disponibilidade += probabilidade_i
    return disponibilidade

# Configuração do painel 2x3
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('Análise de Disponibilidade: 6 Casos de Teste de Proporções', fontsize=16)

probabilidades_p = np.linspace(0, 1, 100)

# --- Gráfico 1: Impacto de k em cluster pequeno (n=5) ---
ax = axes[0, 0]
n_val = 5
for k_val in [1, 3, 5]:
    valores = [disponibilidade_analitica(n_val, k_val, p) for p in probabilidades_p]
    ax.plot(probabilidades_p, valores, label=f'k={k_val}', linewidth=2)
ax.set_title("1. Alterando 'k' (Cluster Pequeno n=5)")
ax.set_xlabel("Probabilidade do Servidor (p)")
ax.set_ylabel("Disponibilidade do Sistema")
ax.legend()
ax.grid(True, linestyle='--', alpha=0.6)

# --- Gráfico 2: Impacto de k em cluster grande (n=20) ---
ax = axes[0, 1]
n_val = 20
for k_val in [1, 10, 20]:
    valores = [disponibilidade_analitica(n_val, k_val, p) for p in probabilidades_p]
    ax.plot(probabilidades_p, valores, label=f'k={k_val}', linewidth=2)
ax.set_title("2. Alterando 'k' (Cluster Grande n=20)")
ax.set_xlabel("Probabilidade do Servidor (p)")
ax.legend()
ax.grid(True, linestyle='--', alpha=0.6)

# --- Gráfico 3: Impacto de p alterando k (Fixo n=15) ---
ax = axes[0, 2]
n_val = 15
eixo_k = list(range(1, n_val + 1))
for p_val in [0.5, 0.7, 0.9]:
    valores = [disponibilidade_analitica(n_val, k, p_val) for k in eixo_k]
    ax.plot(eixo_k, valores, marker='o', label=f'p={p_val}', markersize=4)
ax.set_title("3. Queda de Disponibilidade ao aumentar 'k' (n=15)")
ax.set_xlabel("Mínimo Necessário (k)")
ax.set_xticks(range(1, 16, 2))
ax.legend()
ax.grid(True, linestyle='--', alpha=0.6)

# --- Gráfico 4: O peso de adicionar servidores (Fixo k=2) ---
ax = axes[1, 0]
k_val = 2
eixo_n = list(range(k_val, 16))
for p_val in [0.2, 0.5, 0.8]:
    valores = [disponibilidade_analitica(n, k_val, p_val) for n in eixo_n]
    ax.plot(eixo_n, valores, marker='s', label=f'p={p_val}', markersize=4)
ax.set_title("4. Crescimento ao aumentar 'n' (k=2 Fixo)")
ax.set_xlabel("Total de Servidores (n)")
ax.set_ylabel("Disponibilidade do Sistema")
ax.legend()
ax.grid(True, linestyle='--', alpha=0.6)

# --- Gráfico 5: O cenário de Quórum da Maioria (k = teto(n/2)) ---
ax = axes[1, 1]
cenarios_n = [3, 7, 15]
for n_val in cenarios_n:
    k_quorum = math.ceil(n_val / 2)
    valores = [disponibilidade_analitica(n_val, k_quorum, p) for p in probabilidades_p]
    ax.plot(probabilidades_p, valores, label=f'n={n_val}, k={k_quorum}', linewidth=2)
ax.set_title("5. Escala de Quórum da Maioria (k \u2248 n/2)") # \u2248 é o símbolo de aproximação
ax.set_xlabel("Probabilidade do Servidor (p)")
ax.legend()
ax.grid(True, linestyle='--', alpha=0.6)

# --- Gráfico 6: O cenário de Atualização Síncrona (k = n) ---
ax = axes[1, 2]
eixo_n_sync = list(range(1, 11))
for p_val in [0.9, 0.95, 0.99]:
    valores = [disponibilidade_analitica(n, n, p_val) for n in eixo_n_sync]
    ax.plot(eixo_n_sync, valores, marker='^', label=f'p={p_val}', markersize=5)
ax.set_title("6. Fragilidade da Atualização (k=n)")
ax.set_xlabel("Total de Servidores (n = k)")
ax.set_xticks(eixo_n_sync)
ax.legend()
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()