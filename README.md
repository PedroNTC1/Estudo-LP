# Olá, Professor!

Este projeto foi desenvolvido para comparar a performance de diferentes algoritmos de resolução de sistemas lineares utilizando uma interface interativa com o Streamlit.

## Bibliotecas Necessárias

Para que o projeto funcione corretamente, é necessário instalar as seguintes bibliotecas Python:

- **streamlit**
- **numpy**
- **pandas**

Você pode instalar todas de uma vez usando o comando abaixo no terminal:

```
pip install streamlit numpy pandas
```

## Como Executar

Após instalar as bibliotecas, basta rodar o comando abaixo no terminal, dentro da pasta do projeto:

```
streamlit run app_matriz_interativa.py
```
Ou, caso o comando `streamlit` não seja reconhecido, utilize:
```
python -m streamlit run app_matriz_interativa.py
```

## Observações sobre a Interface

A matriz e o vetor `b` podem ser preenchidos manualmente na interface principal. Em alguns momentos, pode ocorrer instabilidade ou o preenchimento não atualizar imediatamente. Caso isso aconteça, basta clicar novamente para preencher ou editar os valores, que a interface irá atualizar normalmente.

## Resumo do Projeto

Este projeto permite ao usuário definir um sistema de equações lineares (Ax = b) e resolvê-lo utilizando três métodos diferentes: Regra de Cramer, Eliminação Gaussiana e o solver otimizado do NumPy. A aplicação compara o tempo de execução de cada algoritmo e apresenta os resultados de forma visual e interativa, facilitando o entendimento das diferenças de performance entre os métodos.

Espero que

