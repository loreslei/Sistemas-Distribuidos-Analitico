import random
import math
import pandas as pd
import matplotlib.pyplot as plt

def probabilidade_analitica(n, k, p):
    disp = 0
    for i in range(k, n + 1):
        disp += math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
    return disp

def simulador_estocastico(n, k, p, num_rodadas):
    sucessos = 0
    for _ in range(num_rodadas):
        # sum(1 ...) atua como um contador rápido de servidores online
        online = sum(1 for _ in range(n) if random.random() <= p)
        if online >= k:
            sucessos += 1
    return sucessos / num_rodadas

# Parametros do teste
n_teste = 5
k_teste = 3
p_teste = 0.8
teorico = probabilidade_analitica(n_teste, k_teste, p_teste)

# Vamos testar de 10 rodadas ate 50.000 rodadas, dando saltos para acelerar
rodadas_lista = [10, 50, 100, 500, 1000, 2500, 5000, 10000, 25000, 50000]
erros = []
resultados_simulados = []
dados_tabela = [] # Lista dedicada para armazenar os dados do Pandas

print("Calculando a convergência. Isso pode levar alguns segundos...\n")

for N in rodadas_lista:
    simulado = simulador_estocastico(n_teste, k_teste, p_teste, N)
    erro_absoluto = abs(teorico - simulado)
    
    resultados_simulados.append(simulado)
    erros.append(erro_absoluto)
    
    # Adicionando os valores do laço atual na lista para a tabela
    dados_tabela.append({
        'Rodadas (N)': N,
        'Valor Teórico': teorico,
        'Valor Simulado': simulado,
        'Erro Absoluto': erro_absoluto
    })

# --- Criação e exibição da Tabela com Pandas ---
df_convergencia = pd.DataFrame(dados_tabela)
print(f"=== Tabela de Convergência da Simulação (n={n_teste}, k={k_teste}, p={p_teste}) ===")
# Formatando para 5 casas decimais para evidenciar o erro caindo
print(df_convergencia.to_string(index=False, float_format=lambda x: f"{x:.5f}"))
print("\nGerando os gráficos...\n")

# --- Visualização em 2 Subgráficos ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5))

# Gráfico 1: A convergência para a linha teórica
ax1.axhline(y=teorico, color='black', linestyle='--', label=f'Valor Teórico ({teorico:.4f})')
ax1.plot(rodadas_lista, resultados_simulados, marker='o', color='blue', alpha=0.7, label='Valor Simulado')
ax1.set_xscale('log') # Escala logarítmica para ver os saltos exponenciais em N
ax1.set_title('Convergência do Valor Simulado (Escala Log)')
ax1.set_xlabel('Número de Rodadas (N)')
ax1.set_ylabel('Disponibilidade Calculada')
ax1.legend()
ax1.grid(True, alpha=0.4)

# Gráfico 2: A queda do Erro
ax2.plot(rodadas_lista, erros, marker='s', color='red')
ax2.axhline(y=0, color='black', linewidth=1)
ax2.set_xscale('log')
ax2.set_title('Tamanho do Erro Absoluto vs Número de Rodadas')
ax2.set_xlabel('Número de Rodadas (N)')
ax2.set_ylabel('Erro (Teórico - Simulado)')
ax2.grid(True, alpha=0.4)

plt.tight_layout()
plt.show()