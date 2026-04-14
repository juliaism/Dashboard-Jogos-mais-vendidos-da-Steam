# Dashboard-Jogos-mais-vendidos-da-Steam

📝 Descrição 
     O projeto objetivou realizar uma análise da base de dados de jogos comercializados na plataforma Steam, de modo a criar um dashboard interativo, no qual o usuário poderá explorar informações relevantes no que se refere ao segmento gamer.

🗃️ 1. Conjunto de Dados 

• Dataset Utilizado: https://www.kaggle.com/datasets/hbugrae/best-selling-steam-games-of-all-time 

• Justificativa: O Dataset utilizado é de grande relevância, uma vez que trata da maior plataforma de jogos para PC atualmente, e contem uma grande variabilidade de dados permitindo analisar diversos pontos como volume de vendas, popularidade de desenvolvedores e de gênero de jogos, tendências temporais e as correlações entre esses dados

• Formato: CSV

🧹 2. Tratamento de Dados

• Conversão de Dados: A coluna "release_date" é convertida de string para datetime facilitando a extração do ano para a criação da coluna "release_year".

• Limpeza de Dados: Para a ánalise das colunas "user_defined_tags" e "supported_os" foi necessário criar um novo Dataframe contendo apenas as colunas necessárias ("game_name" e "user_defined_tags"/"supported_os"), converter a string dos dados em uma lista, .str.split(','), e depois utilizar .exploed(coluna) para transformar cada elemento af lista em uma nova linha, garantindo que elementos de tags e os sejam lidos individualmente e não em grupo como estão no Dataset, por fim espaços em branco e vazios foram removidos.

• Tratamento de Outliers: Foram identificados outliers que representam menos de 0.1% dos dados e, uma vez que não efetam a análise geral do dataset, não foram excluídos


💡 3. Insights


📚 4. Bibliotecas Utilizadas

 • Pandas
 
 • Matplotlib
 
 • Seaborn
 
 • Streamlit
 
 • Plotly Express
