import math
import random
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Cálculo Analítico (Teórico)
# ---------------------------------------------------------
def disponibilidade_analitica(n, k, p):
    """Calcula a probabilidade exata usando a fórmula da Distribuição Binomial."""
    disponibilidade_total = 0.0
    for i in range(k, n + 1):
        # Combinação (n escolhe i) * p^i * (1-p)^(n-i)
        combinacao = math.comb(n, i)
        probabilidade_i = combinacao * (p ** i) * ((1 - p) ** (n - i))
        disponibilidade_total += probabilidade_i
    return disponibilidade_total

# ---------------------------------------------------------
# 2. Simulador Estocástico (Prático/Experimental)
# ---------------------------------------------------------
def disponibilidade_simulada(n, k, p, num_rodadas=10000):
    """Simula o cenário rodando milhares de testes para achar a frequência."""
    rodadas_sucesso = 0
    
    for _ in range(num_rodadas):
        servidores_disponiveis = 0
        for _ in range(n):
            # Gera número aleatório entre 0.0 e 1.0. Se for <= p, o servidor está UP.
            if random.random() <= p:
                servidores_disponiveis += 1
                
        # Se atingiu o quórum mínimo k, o serviço se manteve operacional
        if servidores_disponiveis >= k:
            rodadas_sucesso += 1
            
    return rodadas_sucesso / num_rodadas

# ---------------------------------------------------------
# 3. Execução e Geração de Gráficos e Tabelas
# ---------------------------------------------------------
n = 5 # Total de servidores
probabilidades_p = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
casos_k = [1, math.ceil(n/2), n] # k=1, k=3 (maioria), k=5 (todos)

print(f"Comparação para n={n}\n")
print(f"{'p':<5} | {'k':<3} | {'Analítico':<10} | {'Simulado':<10} | {'Diferença'}")
print("-" * 45)

plt.figure(figsize=(10, 6))

for k in casos_k:
    valores_analiticos = []
    valores_simulados = []
    
    for p in probabilidades_p:
        analitico = disponibilidade_analitica(n, k, p)
        simulado = disponibilidade_simulada(n, k, p)
        
        valores_analiticos.append(analitico)
        valores_simulados.append(simulado)
        
        # Imprime os resultados na tabela do terminal
        diff = abs(analitico - simulado)
        print(f"{p:.1f}   | {k:<3} | {analitico:.4f}     | {simulado:.4f}     | {diff:.4f}")
        
    # Plota a linha analítica e os pontos simulados para o gráfico
    plt.plot(probabilidades_p, valores_analiticos, label=f'Analítico (k={k})', linewidth=2)
    plt.scatter(probabilidades_p, valores_simulados, label=f'Simulado (k={k})', marker='x')

# Configurações do Gráfico 2D (similar à imagem que você enviou)
plt.title(f'Disponibilidade do Serviço (n={n})')
plt.xlabel('Probabilidade individual do servidor estar UP (p)')
plt.ylabel('Disponibilidade do Sistema')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()