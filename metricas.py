import math
import pandas as pd
import matplotlib.pyplot as plt

def calcular_disponibilidade(n, k, p):
    """Calcula a disponibilidade usando a distribuicao binomial."""
    disp = 0
    for i in range(k, n + 1):
        disp += math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
    return disp

# ===========================================================================
# GERAÇÃO DAS TABELAS (PANDAS)
# ===========================================================================

print("\n" + "="*50)
print("TABELA 1: Variação da Confiabilidade (p) para n=10")
print("="*50)
p_amostra = [0.50, 0.70, 0.85, 0.90, 0.95, 0.99]
k_amostra = [1, 3, 5, 8, 10]
dados_t1 = []

for p in p_amostra:
    linha = {'p (Probabilidade)': p}
    for k in k_amostra:
        linha[f'k={k}'] = calcular_disponibilidade(10, k, p)
    dados_t1.append(linha)

df1 = pd.DataFrame(dados_t1)
print(df1.to_string(index=False, float_format=lambda x: f"{x:.5f}"))

print("\n" + "="*50)
print("TABELA 2: Escalonamento do Cluster (n) com p=0.85")
print("="*50)
dados_t2 = []

for n in range(1, 16, 2): # Testando n ímpares para encurtar a tabela
    dados_t2.append({
        'n (Tamanho Cluster)': n,
        'k=1 (Consulta)': calcular_disponibilidade(n, 1, 0.85),
        'k=n/2 (Quórum)': calcular_disponibilidade(n, math.ceil(n / 2), 0.85),
        'k=n (Estrita)': calcular_disponibilidade(n, n, 0.85)
    })

df2 = pd.DataFrame(dados_t2)
print(df2.to_string(index=False, float_format=lambda x: f"{x:.5f}"))

print("\n" + "="*50)
print("TABELA 3: Tolerância à Restrição (k) para n=10")
print("="*50)
dados_t3 = []
p_testes = [0.5, 0.7, 0.9, 0.99]

for k in range(1, 11):
    linha = {'k (Mín. Exigido)': k}
    for p in p_testes:
        linha[f'p={p}'] = calcular_disponibilidade(10, k, p)
    dados_t3.append(linha)

df3 = pd.DataFrame(dados_t3)
print(df3.to_string(index=False, float_format=lambda x: f"{x:.5f}"))
print("\nGerando os gráficos...\n")


# ===========================================================================
# GERAÇÃO DOS GRÁFICOS
# ===========================================================================

# Criando a figura com 3 subgraficos horizontais
fig, axes = plt.subplots(1, 3, figsize=(20, 6))

# --- Grafico 1: Fixando 'n', variando 'p' para TODOS os 'k' ---
n_fixo_1 = 10
p_vals = [x / 100.0 for x in range(0, 101)]

for k in range(1, n_fixo_1 + 1):
    disp_vals = [calcular_disponibilidade(n_fixo_1, k, p) for p in p_vals]
    axes[0].plot(p_vals, disp_vals, label=f'k={k}')

axes[0].set_title(f'1. Variação de p para todos os k (n={n_fixo_1})')
axes[0].set_xlabel('Probabilidade do Servidor (p)')
axes[0].set_ylabel('Disponibilidade do Sistema')
axes[0].legend(title="Min. Servidores (k)", fontsize=8)
axes[0].grid(True, linestyle='--', alpha=0.6)

# --- Grafico 2: Fixando 'p', variando 'n' para as 3 estrategias ---
p_fixo_2 = 0.85
n_vals = list(range(1, 16))

disp_k1 = [calcular_disponibilidade(n, 1, p_fixo_2) for n in n_vals]
disp_quorum = [calcular_disponibilidade(n, math.ceil(n / 2), p_fixo_2) for n in n_vals]
disp_kn = [calcular_disponibilidade(n, n, p_fixo_2) for n in n_vals]

axes[1].plot(n_vals, disp_k1, marker='o', label='k=1 (Consulta)')
axes[1].plot(n_vals, disp_quorum, marker='^', label='k=n/2 (Quorum)')
axes[1].plot(n_vals, disp_kn, marker='s', label='k=n (Atualização Estrita)')

axes[1].set_title(f'2. Variação de n por Estratégia (p={p_fixo_2})')
axes[1].set_xlabel('Tamanho do Cluster (n)')
axes[1].set_ylabel('Disponibilidade do Sistema')
axes[1].legend()
axes[1].grid(True, linestyle='--', alpha=0.6)

# --- Grafico 3: Fixando 'n', variando 'k' ---
n_fixo_3 = 10
k_vals = list(range(1, n_fixo_3 + 1))

for p in p_testes:
    disp_vals = [calcular_disponibilidade(n_fixo_3, k, p) for k in k_vals]
    axes[2].plot(k_vals, disp_vals, marker='d', label=f'p={p}')

axes[2].set_title(f'3. Tolerância à Restrição k (n={n_fixo_3})')
axes[2].set_xlabel('Exigência Mínima (k)')
axes[2].set_ylabel('Disponibilidade do Sistema')
axes[2].legend(title="Confiabilidade (p)")
axes[2].grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()