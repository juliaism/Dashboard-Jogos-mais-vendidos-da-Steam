# Dashboard-Jogos-mais-vendidos-da-Steam

📝 Descrição 
     O projeto objetivou realizar uma análise da base de dados de jogos comercializados na plataforma Steam, de modo a criar um dashboard interativo, no qual o usuário poderá explorar informações relevantes no que se refere ao segmento gamer.


🗃️ 1. Conjunto de Dados 

• Dataset Utilizado: https://www.kaggle.com/datasets/hbugrae/best-selling-steam-games-of-all-time 

• Justificativa: O Dataset utilizado é de grande relevância, uma vez que trata da maior plataforma de jogos para PC atualmente, e contem uma grande variabilidade de dados permitindo analisar diversos pontos como volume de vendas, popularidade de desenvolvedores e de gênero de jogos, tendências temporais e as correlações entre esses dados

• Formato: CSV


🧹 2. Tratamento de Dados

• Conversão de Dados: A coluna "release_date" é convertida de string para datetime facilitando a extração do ano para a criação da coluna "release_year".

• Limpeza de Dados: Para a ánalise das colunas "user_defined_tags" e "supported_os" foi necessário criar um novo Dataframe contendo apenas as colunas necessárias ("game_name" e "user_defined_tags"/"supported_os"), converter a string dos dados em uma lista, .str.split(','), e depois utilizar .exploed(coluna) para transformar cada elemento da lista em uma nova linha, garantindo que elementos de "tags" e "os" sejam lidos individualmente e não em grupo como estão no Dataset, por fim espaços em branco e vazios foram removidos.

• Tratamento de Outliers: Foram identificados outliers que representam menos de 0.1% dos dados e, uma vez que não efetam a análise geral do dataset, não foram excluídos


💡 3. Insights

1- Destaques: Jogos, Desenvolvedores e Tags

• Top Jogos por Vendas: Domínio de títulos First-Person Shooter (FPS) multiplayer, com vendas acumuladas atingindo até 350 milhões de unidades e representando mais da metade do Top 10

• Top Desenvolvedores: Líderes incluem Valve, responsável pelos top 2 de jogos mais vendidos, seguida por Arc System Works, CAPCOM e ParadoX Develo. 

• Tags Populares: O alto volume em Simulation sugere um público interessado em imersão, enquanto o sucesso de Action destaca a preferência por experiências intensas.

2-  Análise de Relações

• Dificuldade vs Duração: Jogos com maior dificuldade tendem a ter durações maiores. 

• Preço vs Vendas: A grande maioria dos produtos está concentrada na faixa de 0 a 20 USD, tendo os jogos free-to-play na liderança. Passando dessa faixa as vendas diminuem drasticamente, sugerindo um mercado de menor demanda para itens mais caros.

• Vendas por Ano de Lançamento: O gráfico mostra o crescimento da indústria, onde os lançamentos recentes (2024) detêm o recorde de faturamento, mas o catálogo histórico, com jogos presentes no topo da lista de mais vendidos, sustenta a base da plataforma. É importante destacar que os dados foram coletados antes do fim do ano de 2025 e por isso há uma grande queda em comparação aos anos anteriores.


3. Ánalise de Distribuição

• Sistemas Operacionais Suportados: A distribuição reflete uma estratégia de alcance massivo, onde o suporte é otimizado para o Windows, mas mantém a cross-plataformidade essencial para não excluir usuários de outros sistemas.

• Classificação Indicativa: A maior fatia indica que uma grande parte do catálogo da Steam é voltada para o público adulto. Porém, as outras categorias mostram que a Steam possui uma biblioteca diversificada, atendendo todas as faixas etárias.


📚 4. Bibliotecas Utilizadas

 • Pandas
 
 • Matplotlib
 
 • Seaborn
 
 • Streamlit
 
 • Plotly Express
