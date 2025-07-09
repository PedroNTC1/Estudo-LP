import streamlit as st
import numpy as np
import pandas as pd
import time

# --- Funções dos Algoritmos (mesmas da resposta anterior) ---

def resolver_cramer(A, b):
    n = A.shape[0]
    det_A = np.linalg.det(A)
    if np.isclose(det_A, 0):
        raise ValueError("A matriz é singular (determinante zero), Cramer não aplicável.")
    x = np.zeros(n)
    for i in range(n):
        A_i = A.copy()
        A_i[:, i] = b
        x[i] = np.linalg.det(A_i) / det_A
    return x

def resolver_gauss(A, b):
    n = A.shape[0]
    M = np.hstack([A, b.reshape(-1, 1)]).astype(float)
    for k in range(n):
        if np.isclose(M[k, k], 0):
            # Procura uma linha abaixo para trocar (pivotação parcial simples)
            for i in range(k + 1, n):
                if not np.isclose(M[i, k], 0):
                    M[[k, i]] = M[[i, k]] # Troca as linhas
                    break
            else:
                 raise ValueError("Matriz é singular ou requer pivotação complexa.")
        
        for i in range(k + 1, n):
            fator = M[i, k] / M[k, k]
            M[i, k:] = M[i, k:] - fator * M[k, k:]
    
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        soma_ax = np.dot(M[i, i+1:n], x[i+1:])
        x[i] = (M[i, n] - soma_ax) / M[i, i]
    return x

def resolver_numpy(A, b):
    return np.linalg.solve(A, b)

# --- Interface da Aplicação com Streamlit ---

st.set_page_config(layout="wide", page_title="Performance de Solvers")

st.title("📊 Comparador de Performance de Solvers de Sistemas Lineares")
st.markdown("""
Esta aplicação permite que você defina um sistema de equações lineares **Ax = b**, 
resolva-o com três algoritmos diferentes e compare a performance de cada um em tempo real.
""")

# --- Painel de Controle na Barra Lateral ---
with st.sidebar:
    st.header("⚙️ Painel de Controle")
    
    # Slider para definir o tamanho da matriz
    n = st.slider("Selecione o tamanho do sistema (n x n):", min_value=2, max_value=12, value=3, key="n_slider")

    # Aviso sobre a Regra de Cramer
    if n > 8:
        st.warning(f"Atenção: A Regra de Cramer é extremamente lenta para n > 8. A execução para n={n} pode levar muito tempo ou travar o navegador.")

    st.markdown("---")
    st.subheader("Valores do Sistema")

    # Botão para gerar valores aleatórios
    if st.button("Gerar Sistema Aleatório"):
        st.session_state.A = np.random.rand(n, n) * 10
        st.session_state.b = np.random.rand(n, 1) * 10
    
    st.info("Você pode preencher a matriz e o vetor `b` manualmente na tela principal.")

# --- Área Principal para Input da Matriz ---
st.header(f"Sistema de Equações {n}x{n}")

# Inicializa as matrizes no estado da sessão se não existirem
if 'A' not in st.session_state or st.session_state.A.shape[0] != n:
    st.session_state.A = np.zeros((n, n))
if 'b' not in st.session_state or st.session_state.b.shape[0] != n:
    st.session_state.b = np.zeros((n, 1))

# Cria colunas para a matriz A e o vetor b
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("Matriz A")
    grid_A = st.empty()
    df_A = pd.DataFrame(st.session_state.A)
    # Usa o editor de dados do Streamlit para uma entrada fácil
    edited_A = grid_A.data_editor(df_A, key="editor_A", use_container_width=True)
    st.session_state.A = edited_A.to_numpy()

with col2:
    st.subheader("Vetor b")
    grid_b = st.empty()
    df_b = pd.DataFrame(st.session_state.b, columns=["b"])
    edited_b = grid_b.data_editor(df_b, key="editor_b", use_container_width=True)
    st.session_state.b = edited_b.to_numpy().flatten()


st.markdown("---")

# --- Botão para Executar e Mostrar Resultados ---
if st.button("Resolver e Comparar Performance", type="primary", use_container_width=True):
    A = st.session_state.A
    b = st.session_state.b.flatten()

    algoritmos = {
        "Regra de Cramer": resolver_cramer,
        "Eliminação Gaussiana": resolver_gauss,
        "NumPy linalg.solve": resolver_numpy,
    }

    resultados = []
    solucoes = {}

    with st.spinner("Calculando... A Regra de Cramer pode ser lenta."):
        for nome, func in algoritmos.items():
            # Pula Cramer se o sistema for muito grande
            if nome == "Regra de Cramer" and n > 10:
                resultados.append({"Algoritmo": nome, "Tempo (s)": "N/A (muito lento)"})
                solucoes[nome] = "N/A"
                continue

            try:
                inicio = time.time()
                solucao = func(A.copy(), b.copy())
                fim = time.time()
                duracao = fim - inicio
                
                resultados.append({"Algoritmo": nome, "Tempo (s)": duracao})
                solucoes[nome] = solucao

            except Exception as e:
                st.error(f"O algoritmo '{nome}' falhou: {e}")
                resultados.append({"Algoritmo": nome, "Tempo (s)": "Erro"})
                solucoes[nome] = f"Erro: {e}"
    
    st.success("Cálculos finalizados!")
    
    st.header("🔍 Resultados")

    # --- Mostra as Soluções ---
    st.subheader("Soluções Encontradas (vetor x)")
    cols_sol = st.columns(len(algoritmos))

    for i, (nome, sol) in enumerate(solucoes.items()):
        with cols_sol[i]:
            st.metric(label=nome, value="")
            if isinstance(sol, np.ndarray):
                st.dataframe(pd.DataFrame(sol, columns=['x']), use_container_width=True)
            else:
                st.write(sol)

    # --- Mostra a Performance ---
    st.subheader("Comparativo de Performance")
    df_resultados = pd.DataFrame(resultados)
    
    # Limpa dados para o gráfico (remove erros e N/A)
    df_plot = df_resultados[pd.to_numeric(df_resultados['Tempo (s)'], errors='coerce').notna()].copy()
    df_plot['Tempo (s)'] = df_plot['Tempo (s)'].astype(float)
    
    col_tabela, col_grafico = st.columns([1, 2])

    with col_tabela:
        st.write("Tabela de Tempos:")
        st.dataframe(df_resultados, use_container_width=True, hide_index=True)

    with col_grafico:
        st.write("Gráfico de Performance:")
        if not df_plot.empty:
            st.bar_chart(df_plot.set_index("Algoritmo"))
        else:
            st.info("Não há dados de performance para exibir no gráfico.")