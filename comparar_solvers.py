import numpy as np
import time

# --- ALGORITMO 1: REGRA DE CRAMER ---
# Complexidade: O(n!) - Extremamente lento para sistemas maiores.
def resolver_cramer(A, b):
    """
    Resolve um sistema de equações Ax = b usando a Regra de Cramer.
    Funciona apenas para matrizes quadradas com solução única.
    """
    n = A.shape[0]
    # Calcula o determinante da matriz principal
    det_A = np.linalg.det(A)

    if det_A == 0:
        # Se o determinante for zero, não há solução única.
        return None

    # Inicializa o vetor de solução
    x = np.zeros(n)

    # Itera sobre cada variável para encontrar sua solução
    for i in range(n):
        # Cria uma cópia da matriz A para modificação
        A_i = A.copy()
        # Substitui a i-ésima coluna pelo vetor b
        A_i[:, i] = b
        # A solução x_i é det(A_i) / det(A)
        x[i] = np.linalg.det(A_i) / det_A

    return x

# --- ALGORITMO 2: ELIMINAÇÃO GAUSSIANA ---
# Complexidade: O(n^3) - Muito mais eficiente que Cramer.
def resolver_gauss(A, b):
    """
    Resolve um sistema de equações Ax = b usando Eliminação Gaussiana
    com retrosubstituição. Implementado "do zero".
    """
    n = A.shape[0]
    # 1. Construir a matriz aumentada [A|b]
    M = np.hstack([A, b.reshape(-1, 1)])
    M = M.astype(float) # Garante que temos números de ponto flutuante

    # 2. Fase de Eliminação (Triangulação)
    for k in range(n):
        # Pivotação: Se o pivô for zero, a implementação simples falha.
        # Uma implementação robusta trocaria linhas (pivotação parcial).
        if M[k, k] == 0:
            # Para este exemplo, retornamos erro.
            raise ValueError("Pivô zero encontrado. A implementação requer pivotação.")

        # Itera sobre as linhas abaixo do pivô
        for i in range(k + 1, n):
            fator = M[i, k] / M[k, k]
            # Subtrai a linha do pivô multiplicada pelo fator
            M[i, k:] = M[i, k:] - fator * M[k, k:]

    # 3. Fase de Retrosubstituição
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        soma_ax = np.dot(M[i, i+1:n], x[i+1:])
        x[i] = (M[i, n] - soma_ax) / M[i, i]

    return x

# --- ALGORITMO 3: SOLVER OTIMIZADO NUMPY ---
# Complexidade: O(n^3) - Mas altamente otimizado em baixo nível (Fortran/C).
def resolver_numpy(A, b):
    """
    Resolve o sistema Ax = b usando a função otimizada do NumPy.
    """
    return np.linalg.solve(A, b)

# --- FUNÇÃO DE VERIFICAÇÃO DE PERFORMANCE ---
def verificar_performance(tamanho_sistema):
    """
    Gera um sistema aleatório do tamanho especificado e mede o tempo
    de execução de cada algoritmo de resolução.
    """
    print("-" * 50)
    print(f"Verificando performance para sistema {tamanho_sistema}x{tamanho_sistema}")
    print("-" * 50)

    # Gera um sistema aleatório com solução garantida
    A = np.random.rand(tamanho_sistema, tamanho_sistema) * 10
    b = np.random.rand(tamanho_sistema) * 10

    # Dicionário dos algoritmos a serem testados
    algoritmos = {
        "Regra de Cramer": resolver_cramer,
        "Eliminação Gaussiana (Pura)": resolver_gauss,
        "NumPy linalg.solve": resolver_numpy,
    }

    for nome, func in algoritmos.items():
        # A Regra de Cramer é inviável para sistemas maiores que 10x10.
        # Vamos pulá-la para não travar o script por horas.
        if nome == "Regra de Cramer" and tamanho_sistema > 10:
            print(f"{nome}: Ignorado (muito lento para este tamanho de sistema).")
            continue
            
        try:
            inicio = time.time()
            solucao = func(A, b)
            fim = time.time()
            duracao = fim - inicio
            print(f"{nome}: {duracao:.6f} segundos.")
        except Exception as e:
            print(f"{nome}: Falhou com o erro - {e}")

# --- EXECUÇÃO PRINCIPAL ---
if __name__ == "__main__":
    # Teste com um sistema pequeno (todos os métodos devem funcionar)
    verificar_performance(3)
    
    # Teste com um sistema médio (Cramer já começa a ficar lento)
    verificar_performance(8)
    
    # Teste com um sistema maior (Cramer é ignorado)
    verificar_performance(100)
    
    # Teste com um sistema muito maior para ver a performance de Gauss vs NumPy
    verificar_performance(500)