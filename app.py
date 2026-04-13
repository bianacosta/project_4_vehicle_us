import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURAÇÃO E LIMPEZA ---
# Lembre-se de verificar se o nome do arquivo é 'vehicles.csv' ou 'vehicles_us.csv'
car_data = pd.read_csv('vehicles.csv')

# Limpeza dos dados (essencial para os gráficos não quebrarem)
car_data['is_4wd'] = car_data['is_4wd'].fillna(0).astype(int)
car_data['paint_color'] = car_data['paint_color'].fillna('unknown')
car_data['model_year'] = car_data['model_year'].fillna(
    car_data['model_year'].median()).astype(int)
car_data['cylinders'] = car_data['cylinders'].fillna(
    car_data['cylinders'].median()).astype(int)
car_data['odometer'] = car_data['odometer'].fillna(
    car_data['odometer'].median())

# --- INTERFACE DO USUÁRIO ---
st.title('Dashboard de Análise: Venda de Veículos nos EUA')
st.write('Explore as tendências de mercado e preços de carros usados de forma interativa.')
st.divider()

st.header('Exploração de Dados')

# Criando botões para disparar os gráficos
hist_button = st.button('Criar histograma de quilometragem')

# --- SEÇÃO 1: USANDO BOTÕES ---
# Lógica do Histograma
if hist_button:
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig_hist = px.histogram(car_data, x="odometer",
                            title="Distribuição de Odômetros")
    st.plotly_chart(fig_hist, use_container_width=True)

# --- SEÇÃO 2: USANDO CAIXA DE SELEÇÃO ---
st.header('Visualizações Fixas')
st.write('Marque a caixa para manter o gráfico de dispersão visível para análise.')
show_scatter = st.checkbox('Exibir Gráfico de Dispersão (Odômetro vs Preço)')

if show_scatter:
    fig_scatter = px.scatter(car_data, x="odometer",
                             y="price", title="Relação: Odômetro vs Preço")
    st.plotly_chart(fig_scatter, use_container_width=True)
