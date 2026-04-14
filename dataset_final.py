# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# %%
df = pd.read_csv(r"C:\Users\jjate\Downloads\bestSelling_games.csv")


# %% [markdown]
# # Inspecao basica

# %%
df.head()

# %%
df.tail()

# %%
df.info()

# %%
df.describe()

# %%
df.shape

# %% [markdown]
# ### Frequencia dos itens das colunas
# 

# %%
print(df['developer'].value_counts())
print("--------------")
print(df['user_defined_tags'].value_counts())
print("--------------")
print(df['supported_os'].value_counts())


# %%
print(df['age_restriction'].value_counts())
print("--------------")
print(df['price'].value_counts())
print("--------------")
print(df['supported_languages'].value_counts())


# %%
print(df['rating'].value_counts())
print("--------------")
print(df['difficulty'].value_counts())
print("--------------")
print(df['length'].value_counts())

# %% [markdown]
# ### Shapes

# %%
print('ratings:', (df.rating.value_counts()).shape)
print('developers:', (df.developer.value_counts()).shape)
print('difficulty:', (df.difficulty.value_counts()).shape)
print('age_restriction:', (df.age_restriction.value_counts()).shape)



# %% [markdown]
# ### Quantidade de valores unicos 

# %%
print('ratings:', (df.rating.value_counts()).nunique())
print('difficulty:', (df.difficulty.value_counts()).nunique())
print('age_restriction:', (df.age_restriction.value_counts()).nunique())
print('developer:', (df.developer.value_counts()).nunique())
print('supported_os:', (df.supported_os.value_counts()).nunique())
print('supported_languages:', (df.supported_languages.value_counts()).nunique())
print('other_features:', (df.other_features.value_counts()).nunique())



# %% [markdown]
# ### Valores nulos
# 

# %%
df.isna().sum()

# %% [markdown]
# ### Valores duplicados

# %%
df.duplicated().sum()

# %% [markdown]
# ### Converter string para datetime

# %%
df['release_date']=pd.to_datetime(df['release_date'])
df.dtypes

# %% [markdown]
# ### Criar nova coluna ano de lancamento

# %%
df['release_year'] = df['release_date'].dt.year
df.info()
df.head()
df['release_year'].value_counts()

# %% [markdown]
# ### Identificar outliers

# %%
contagem_os = df['supported_os'].value_counts()
outliers_os = contagem_os[contagem_os < 5]
print(outliers_os)

# %% [markdown]
# # Analise exploratoria de dados

# %% [markdown]
# ### Top 10 tags e desenvolvedores

# %%
top_tags = df['user_defined_tags'].value_counts().head(10).sort_values(ascending=True)
top_tags.plot(kind='barh')
plt.title("Top 10 Tags")
plt.xlabel("Quantidade")
plt.ylabel("Tags")
plt.show()

# %%
top_developers = df['developer'].value_counts().head(10).sort_values(ascending=True)
top_developers.plot(kind='barh')
plt.title("Top 10 Developers")
plt.xlabel("Quantidade")
plt.ylabel("Developers")
plt.show()

# %% [markdown]
# ### Relacao dificuldade x tempo

# %%
sns.lineplot(data=df, x='length', y='difficulty', errorbar=None)
plt.title("Game Length vs Difficulty")
plt.xlabel("Length (hours)")
plt.ylabel("Difficulty")
plt.tight_layout()
plt.show()

print(df[["length", "difficulty"]].corr())

# %% [markdown]
# ### Relacao preco x vendas

# %%
sns.scatterplot(data=df, x='price', y='estimated_downloads')
plt.title("Game Price vs Estimated Downloads")
plt.xlabel("Price ($)")
plt.ylabel("Estimated Downloads")
plt.tight_layout()
plt.show()

print(df[["price", "estimated_downloads"]].corr())

# %% [markdown]
# ### Relacao vendas por tag

# %%
tag_sales = df.groupby('user_defined_tags')['estimated_downloads'].sum().reset_index()

top_tags = tag_sales.sort_values(by='estimated_downloads', ascending=False).head(20)

plt.figure(figsize=(12, 8))
sns.barplot(x='estimated_downloads', y='user_defined_tags', data=top_tags)
plt.title('Top Tags por Vendas')
plt.xlabel('Total Estimated Downloads (Millions)')
plt.ylabel('User Tag')
plt.show()

# %%
df.to_csv('dataset_final.csv', index=False)


