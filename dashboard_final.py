# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

#Configurações do Streamlit
st.set_page_config(page_title="Dashboard de Vendas da Steam", layout="wide")
st.title("Análise de Jogos Mais Vendidos na Steam")

# Carregamento dos dados
st.cache_data
def load_data():
    df = pd.read_csv('dataset_final.csv')
    return df

df = load_data()


# Filtros na barra lateral de tamanho dos gráficos
st.sidebar.header("Filtros de tamanho dos gráficos")
top_vendas_filtradas = st.sidebar.slider("Top Jogos por Vendas", 5, 20, 10)
top_devs_filtradas = st.sidebar.slider("Top Desenvolvedores", 5, 20, 10)
top_tags_filtradas = st.sidebar.slider("Top Tags Definidas por Usuários", 5, 20, 10)

# 1. Top Vendas, Desenvolvedores e Tags
st.header("Top Vendas, Desenvolvedores e Tags")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("Top Jogos Mais Vendidos")
    top_vendas = df.groupby('game_name')['estimated_downloads'].sum().sort_values(ascending=False).head(top_vendas_filtradas)
    st.bar_chart(top_vendas, x_label="Jogos", y_label="Vendas", sort="-estimated_downloads")

with col2:
    st.markdown("Top Desenvolvedores")
    top_devs = df['developer'].value_counts().head(top_devs_filtradas)
    st.bar_chart(top_devs, x_label="Desenvolvedores", y_label="Quantidade de Jogos", sort="-count")
    

with col3:
       
     # Explode user_defined_tags para contar corretamente e filtra para evitar muitos registros
     df_tags = df[['game_name', 'user_defined_tags']]
     df_tags = df_tags.assign(user_defined_tags=df_tags['user_defined_tags'].str.split(',')).explode('user_defined_tags')
     df_tags['user_defined_tags'] = df_tags['user_defined_tags'].str.strip()
     df_tags = df_tags[df_tags['user_defined_tags'] != '']

     top_tags = df_tags['user_defined_tags'].value_counts().head(top_tags_filtradas)
     top_tags_df = top_tags.reset_index()

    # Renomeia colunas e define 'Tags' como índice para exibir os nomes corretamente
     top_tags_df.columns = ['Tags', 'Quantidade']
     top_tags_df = top_tags_df.set_index('Tags')
     st.markdown("Top Tags Definidas por Usuário")
     st.bar_chart(top_tags_df, x_label="Tags", y_label="Quantidade", sort="-Quantidade")
   
# 2. Relacoes
st.header("Análise de Relações")

# Relação entre Dificuldade e duração da gameplay 
sns.set_style("whitegrid")
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=df,x='difficulty',y='length',ax=ax,color='#1f77b4', errorbar=None)
st.markdown("Dificuldade vs Duração da Gameplay")
ax.set_xlabel('Dificuldade', fontsize=12, color='white')
ax.set_ylabel('Duração da Gameplay (Horas)', fontsize=12, color='white')
ax.tick_params(colors='white')
st.plotly_chart(fig)

fig = px.scatter(df,x="price", y="estimated_downloads",hover_name="game_name",color="price",
    labels={
        "price": "Preço (USD)",
        "estimated_downloads": "Vendas",
        "color": "Preço do Jogo"
    }
)

fig.update_layout(template="plotly_dark")
st.markdown("Preço vs Vendas")
st.plotly_chart(fig, use_container_width=True)

#Vendas por preco
st.markdown("Vendas por Preço") 
price_sales = df.groupby('price')['estimated_downloads'].sum().sort_values(ascending=False).head(5)
st.bar_chart(price_sales, sort="-estimated_downloads", x_label="Preço (USD)", y_label="Vendas")

#Vendas por Ano de Lançamento
st.markdown("Vendas por Ano de Lançamento")
release_year_sales = df.groupby('release_year', as_index=False)['estimated_downloads'].sum()
release_year_sales = release_year_sales.sort_values(by='estimated_downloads', ascending=True)
release_year_sales = release_year_sales.set_index('release_year')
st.bar_chart(release_year_sales['estimated_downloads'], x_label="Anos", y_label="Vendas")



# 3. Análise de Distribuição
st.header("Análise de Distribuição")

# Sistema Operacional Suportado
df_os = df[['game_name', 'supported_os']]
df_os = df_os.assign(supported_os=df_os['supported_os'].str.split(',')).explode('supported_os')
df_os['supported_os'] = df_os['supported_os'].str.strip()
df_os = df_os[df_os['supported_os'] != '']

top_os = df_os['supported_os'].value_counts().head(3)
fig_os = px.pie(values=top_os.values, names=top_os.index)
st.markdown("Distribuição dos Sistemas Operacionais Suportados")
st.plotly_chart(fig_os, use_container_width=True)

# restricao de idade
df_age = df[['game_name', 'age_restriction']]
top_age = df_age['age_restriction'].value_counts().head()
top_age_df = top_age.reset_index()

fig_languages = px.pie(values=top_age.values, names=top_age.index)
st.markdown("Distribuição da Restrição de Idade")
st.plotly_chart(fig_languages, use_container_width=True)

# Exibir os dados brutos
if st.checkbox("Mostrar dados brutos"):
    st.dataframe(df)
    
    




