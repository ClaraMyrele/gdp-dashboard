
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Título da página
st.title("Explorador de Voos - Estilo Kayak")

# Carregar os dados
data = np.load('airline_tickets.npy')

# Convertendo os dados em um DataFrame para facilitar a manipulação
colunas = ['cidade_partida', 'cidade_chegada', 'data_viagem', 'companhia_aerea', 'preco']
df = pd.DataFrame(data, columns=colunas)

# Input do usuário
st.sidebar.header("Filtros de Busca")
cidade_partida = st.sidebar.selectbox('Cidade de Partida', df['cidade_partida'].unique())
cidade_chegada = st.sidebar.selectbox('Cidade de Chegada', df['cidade_chegada'].unique())
data_viagem = st.sidebar.date_input('Data de Viagem')
companhia_aerea = st.sidebar.selectbox('Companhia Aérea', df['companhia_aerea'].unique())

# Análise dos dados
X = df.drop('preco', axis=1)
y = df['preco']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalonamento dos dados
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Modelo de Regressão
model = GradientBoostingRegressor()
model.fit(X_train_scaled, y_train)

# Filtros com base nas entradas
voos_filtrados = df[(df['cidade_partida'] == cidade_partida) &
                    (df['cidade_chegada'] == cidade_chegada) &
                    (df['data_viagem'] == data_viagem.strftime('%Y-%m-%d')) &
                    (df['companhia_aerea'] == companhia_aerea)]

# Prevendo os preços dos voos filtrados
if not voos_filtrados.empty:
    X_filtrado = voos_filtrados.drop('preco', axis=1)
    X_filtrado_escalado = scaler.transform(X_filtrado)
    voos_filtrados['preco_previsto'] = model.predict(X_filtrado_escalado)

    # Ordenar voos pelo preço previsto
    voos_filtrados = voos_filtrados.sort_values('preco_previsto')
    
    # Exibir resultados
    st.write(f"Resultados da busca para {cidade_partida} → {cidade_chegada} em {data_viagem}:")
    st.table(voos_filtrados[['cidade_partida', 'cidade_chegada', 'data_viagem', 'companhia_aerea', 'preco_previsto']])
else:
    st.write("Nenhum voo encontrado com os critérios selecionados.")
