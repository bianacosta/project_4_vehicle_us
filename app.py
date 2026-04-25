import pandas as pd
import plotly.express as px
import streamlit as st

# Configuração da página (opcional, mas melhora o visual)
st.set_page_config(page_title="Análise de Veículos", layout="wide")

st.header('Dashboard Interativo: Análise de Inventário de Veículos')

# Lendo os dados
car_data = pd.read_csv('vehicles_us.csv')

# --- BARRA LATERAL (FILTROS) ---
st.sidebar.header("Filtros de Visualização")

# Filtro 1: Seleção de Fabricante (ou Modelo)
# Criamos uma lista de opções únicas para o usuário escolher
model_list = sorted(car_data['model'].unique())
selected_model = st.sidebar.multiselect('Selecione os modelos:', model_list, default=model_list[:5])

# Filtro 2: Range de Preço
min_price, max_price = int(car_data['price'].min()), int(car_data['price'].max())
price_range = st.sidebar.slider("Faixa de Preço", min_price, max_price, (min_price, max_price))

# --- FILTRAGEM DOS DADOS ---
# Aplicamos as escolhas do usuário ao DataFrame original
df_filtered = car_data[
    (car_data['model'].isin(selected_model)) & 
    (car_data['price'].between(price_range[0], price_range[1]))
]

# --- ÁREA DE GRÁFICOS ---
st.subheader('Exploração Visual')

col1, col2 = st.columns(2)

with col1:
    st.write("### Distribuição por Ano")
    show_hist = st.checkbox('Exibir Histograma de Anos', value=True)
    if show_hist:
        fig_hist = px.histogram(df_filtered, x="model_year", color="condition",
                                title="Frequência por Ano e Condição")
        st.plotly_chart(fig_hist, use_container_width=True)

with col2:
    st.write("### Relação Preço vs Odômetro")
    show_scatter = st.checkbox('Exibir Gráfico de Dispersão', value=True)
    if show_scatter:
        fig_scatter = px.scatter(df_filtered, x="odometer", y="price", 
                                 color="type", hover_data=['model'],
                                 title="Preço por Quilometragem")
        st.plotly_chart(fig_scatter, use_container_width=True)

# Exibição da tabela de dados filtrados para conferência
if st.checkbox('Mostrar tabela de dados filtrados'):
    st.dataframe(df_filtered)
