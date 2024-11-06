# Importando as bibliotecas necessárias
from Functions import Funcoes
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
from PIL import Image, ImageDraw
import base64
from io import BytesIO

# Carregando o banco de dados
df = pd.read_csv('data/fitness_gym.csv')

# Exibindo a imagem centralizada na barra lateral
Funcoes.display_centered_image('src/imgs/nesfitv2.jpg')
st.sidebar.image('src\\imgs\\satisfaction_stars.png')

# Cria um seletor de navegação na barra lateral
chart_type = st.sidebar.selectbox("Navegação", ["Tela de Início", "Mercado", "Planos", "Atividades", "Frequência", "Informações do Projeto", "Informações do Grupo"])

# Função para converter imagem em base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Página da Tela de Início
if chart_type == "Tela de Início":
    img_path = "src/imgs/Tela_Inicial.jpg"
    img_base64 = get_base64_of_bin_file(img_path)

    # Aplica o background com a imagem em base64
    background_style = f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{img_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """
    st.markdown(background_style, unsafe_allow_html=True)

# Página do Mercado
elif chart_type == "Mercado":
    # Duas colunas para o contexto de Mercado
    col1, col2 = st.columns(2)
    with col1:
        st.image('src\\imgs\\gym_mercado.png')
    with col2:
        st.markdown("<h1 style='text-align: center;'>Contexto de mercado</h1>", unsafe_allow_html=True)
        st.markdown("""
            ***********************
            #### - O mercado fitness é uma área ampla que contempla negócios voltados à saúde e bem-estar de modo geral.
            #### - Durante as últimas décadas, a necessidade de exercícios físicos é cada vez maior, a crescente preocupação com a saúde fez com que mais pessoas procurassem academias e espaços fitness.
            """)

    st.markdown("""************************""")

    # Duas colunas para as estatísticas de mercado
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h1 style='text-align: center;'>Estatísticas do mercado</h1>", unsafe_allow_html=True)
        st.markdown("""
            *******************
            #### -O mercado fitness no Brasil fatura R$ 12 bilhões ao ano, de acordo com o Panorama Setorial de 2023.
            #### -O valor transacionado com academias e produtos fitness cresceu cerca de 35% em 2023 comparado ao ano anterior, segundo estudo do Itaú Unibanco.
            """)
    with col2:
        st.image('src\\imgs\\gym_mercado2.png')

# Página dos Planos

elif chart_type == "Planos":
    st.markdown("<h1 style='text-align: center;'>Estudo dos Planos</h1>", unsafe_allow_html=True)

    ## Porcentagem de Alunos por Plano
    st.write("### Porcentagem de Alunos por Plano")
    st.pyplot(Funcoes.distribuicao_assinaturas(df))
    
    st.markdown("""
    ### Observação:
    - **O plano Básico engloba mais de 50% do público da academia.**

    *******************************
    """)

    ## Cancelamentos por Tipo de Plano (Motivos)
    st.write("### Cancelamentos por Tipo de Plano (Motivos)")
    st.pyplot(Funcoes.cancelamento_plano(df))
    
    st.markdown("""
    ### Principais Motivos de Cancelamento:
    - **Insatisfação**: 40%
    - **Custo alto**: 25%
    - **Falta de tempo**: 20%

    ### Cancelamentos por Plano:
    - **Basic**: 80%
      - **Principais Motivos**:
        - Insatisfação
        - Custo alto

    - **Premium**: 20%
      - **Principais Motivos**:
        - Falta de tempo
        - Custo alto

    *******************************
    """)

    ## Satisfação Média por Plano
    st.markdown("<h1 style='text-align: center;'>Satisfação Média por Plano</h1>", unsafe_allow_html=True)
    st.pyplot(Funcoes.satisfacao_plano(df))
    
    st.markdown("""
    ### Observação:
    - **Classificação do plano básico está bem abaixo dos outros.**

    *******************************
    """)


    # Problemas e soluções
    st.write("<h1 style='text-align: center;'>Problemas e soluções</h1>", unsafe_allow_html=True)
    st.markdown("""
### Problemas e Estratégias para o Plano Básico da Academia

## Problema Identificado
- **Plano básico** é a principal causa de **críticas e cancelamentos** na academia.

## Motivo das Reclamações
- Assinantes consideram o plano básico **caro e insatisfatório** em relação aos serviços oferecidos.

---

## Impacto dos Cancelamentos

- **80% dos cancelamentos** estão no plano básico.
- **Risco de perda significativa de receita**:
  - 50% dos frequentadores utilizam o plano básico.
  - Persistência dessa tendência pode levar à **falência da academia** devido à redução de receita e custos fixos constantes.

---

## Medida Proposta

### Reavaliação de Preço do Plano Básico
- **Objetivo**: Reduzir o preço do plano básico para torná-lo mais atrativo.

### Desafios no Ajuste de Preço
- Ajustes de preço devem ser **feitos com cautela**, avaliando o impacto tanto para clientes quanto para a academia.
- **Compensação da receita**:
  - Cortes em gastos operacionais.
  - Ajustes nos preços de outros planos.

---

## Prejuízos Além dos Financeiros

- **Imagem e Avaliação**: Problemas no plano básico afetam a reputação da academia.
- **Relacionamento Enfraquecido**: A insatisfação reflete um distanciamento da academia com seus assinantes.

---

## Importância de uma Boa Experiência

- A academia deve oferecer **mais que um produto** — deve proporcionar uma **experiência positiva**.
- **Desafio de Retenção**:
  - A perda de clientes antigos representa um problema, pois **fidelizar novos clientes é mais difícil e custoso**.

---

## Estratégias para Fortalecer Relação com Clientes

- **Ações de Relacionamento**:
  - Pequenas ações, como **confraternizações**, podem fortalecer o vínculo com assinantes do plano básico.
  - Esses eventos permitem à academia **ouvir as queixas** dos clientes e demonstrar que eles são valorizados.

---

## Impacto Financeiro das Iniciativas

- Embora exijam algum investimento, essas ações de **fortalecimento de relacionamento** podem trazer estabilidade e reduzir a taxa de cancelamentos, contribuindo para o sucesso a longo prazo da academia.

    """)


# Estudo das Atividades

elif chart_type == "Atividades":
    st.write("<h1 style='text-align: center;'>Estudo das Atividades</h1>", unsafe_allow_html=True)
    
    ## Atividades mais realizadas
    st.write("### Atividades Mais Realizadas")
    st.pyplot(Funcoes.distribuicao_atividades(df))
    
    st.markdown("""
    ### Top 3 Atividades Mais Realizadas:
    - **1. Zumba**
    - **2. Yoga**
    - **3. Musculação**

    *******************************
    """)

    ## Calorias x Atividades
    st.write("### Calorias x Atividades")
    st.write("#### Média de Calorias Queimadas por Atividade")
    st.pyplot(Funcoes.calorias_atividade(df))
    
    st.markdown("""
    ### Top 3 Atividades com Mais Calorias Queimadas:
    - **1. CrossFit**
    - **2. Spinning**
    - **3. Boxing**

    *******************************
    """)

    ## Distribuição das Idades dos Participantes
    st.write("### Distribuição das Idades dos Participantes")
    st.pyplot(Funcoes.distribuicao_idades(df))
    
    st.markdown("""
    - **Idade Média dos Participantes**: 42 anos
    - **Idade Mínima Encontrada**: 18 anos
    - **Idade Máxima Encontrada**: 64 anos

    *******************************
    """)

    ## Categoria das Atividades
    st.write("### Categoria das Atividades")
    st.pyplot(Funcoes.activity_category(df))
    
    st.markdown("""
    ### Principais Categorias:
    - **1. Bem-estar**
    - **2. Dança**
    - **3. Força**
    """)



    # Problemas e soluções
    st.write("<h1 style='text-align: center;'>Problemas e soluções</h1>", unsafe_allow_html=True)
    st.markdown("""
### Substituição da Atividade de Jump para Otimização do Desempenho

## Identificação do Problema

- **Baixo desempenho da atividade de Jump**:
  - Menor frequência de alunos.
  - Baixa queima de calorias
  - Menor tempo médio de treino.
  - Baixa popularidade entre os frequentadores.

---

## Proposta de Solução

### Substituir o Jump por Atividades como Zumba e Yoga
- **Motivação**: Zumba e Yoga são mais populares e frequentadas pelo público da academia.

### Razões para a Substituição
- **Público-alvo**:
  - Predominância de **pessoas de meia-idade**, que preferem atividades de **baixa intensidade** e com **caráter coletivo**, favorecendo a socialização.
  
- **Tendências de Mercado**:
  - Crescimento do interesse por **saúde e bem-estar**.
  - Yoga e Zumba atendem bem a essa demanda, alinhando-se às expectativas dos frequentadores.

---

## Impulso das Redes Sociais

- **Popularidade da Zumba**:
  - Ganhou visibilidade nas plataformas TikTok e Instagram, especialmente através de eventos de fitdance.
  - Redes sociais ajudam a expandir o alcance da academia e a fortalecer o vínculo com os frequentadores.

---

## Vantagens Econômicas

- **Baixo custo de manutenção**:
  - Yoga e Zumba não exigem equipamentos especializados, o que reduz os custos de manutenção e instalação.
  - Evita problemas fiscais relacionados à preservação de equipamentos.

- **Sustentabilidade Financeira**:
  - A substituição do Jump por Zumba e Yoga visa uma **melhoria estratégica e financeiramente sustentável** para o desempenho da academia.

    """)

# Página das Frequências
elif chart_type == "Frequência":
    st.markdown("<h1 style='text-align: center;'>Estudo das Frequências</h1>", unsafe_allow_html=True)

    ## Frequência Diária dos Alunos
    st.write("### Frequência Diária dos Alunos")
    st.pyplot(Funcoes.frequencia_dia(df))
    
    st.markdown("""
    ### Horário de Funcionamento:
    - **06:00 às 22:00**

    ### Horários de Pico:
    - **17:00 às 18:00**

    ### Horários Vazios:
    - **09:00 às 10:00**
    - **10:00 às 11:00**
    - **14:00 às 15:00**
    - **16:00 às 17:00**

    *******************************
    """)

    ## Frequência Mensal dos Alunos
    st.write("### Frequência Mensal dos Alunos")
    st.pyplot(Funcoes.frequencia_mes(df))
    
    st.markdown("""
    ### Meses Mais Cheios:
    - **Maio**
    - **Setembro**
    - **Outubro**

    ### Meses Mais Vazios:
    - **Janeiro**
    - **Fevereiro**
    - **Abril**

    *******************************
    """)


    # Problemas e soluções
    st.write("<h1 style='text-align: center;'>Problemas e soluções</h1>", unsafe_allow_html=True)
    st.markdown("""
### Otimização de Fluxo e Redução de Custos na Academia               

## Problema Identificado
- **Defasagem nas movimentações dos clientes** ao longo do dia, com períodos de inatividade de 4 a 5 horas.
- **Horários de Inatividade**:
  - **Manhã**: 8h às 10h
  - **Tarde**: 13h às 16h
- Inatividade **considerada anormal**, pois gera custos fixos sem gerar receita.

---

## Impactos Econômicos

### 1. Custo com Energia
- **Valor por hora**: R\$ 22/hora
- **Prejuízo diário**: 5h x R\$ 22 = **R\$ 110**
- **Prejuízo mensal**: R\$ 110 x 30 dias = **R\$ 3.300**
- **Prejuízo anual**: R\$ 3.300 x 12 meses = **R\$ 39.600**

### 2. Custo com Limpeza
- Limpeza **contínua nos períodos de inatividade** gera custo extra com água, produtos e mão de obra, sem retorno financeiro.

### 3. Custo com Salários de Funcionários
- **Custo por funcionário**: R\$ 13/hora
- **Gasto diário** para 1 funcionário (5h): 5h x R\$ 13 = **R\$ 65**
- **Gasto diário total** para 15 funcionários: R\$ 65 x 15 = **R\$ 975**
- **Gasto mensal**: R\$ 975 x 30 dias = **R\$ 29.250**
- **Gasto anual**: R\$ 29.250 x 12 meses = **R\$ 351.000**

---

## Solução Proposta

### Realocação de Clientes
- **Objetivo**: Realocar clientes dos horários de pico para os períodos de inatividade.
  
### Benefícios:
- **Otimização do fluxo** da academia.
- **Melhor gestão de demandas**, trazendo mais equilíbrio ao uso do espaço.
- **Qualidade de trabalho** dos funcionários:
  - Rotinas mais equilibradas
  - Redução de estresse
  - Aumento da produtividade
- **Benefícios para os clientes**:
  - Menor competição pelos equipamentos
  - Experiência de treino mais confortável

---

## Conclusão
A realocação dos clientes pode:
- Reduzir os custos com energia e salários de funcionários
- Melhorar a experiência de trabalho dos funcionários
- Proporcionar um ambiente de treino mais equilibrado e eficiente


    """)

# Informações do projeto
elif chart_type == "Informações do Projeto":
    st.markdown("<h1 style='text-align: center;'>Informações do projeto</h1>", unsafe_allow_html=True)
    st.markdown("""
****************************
# Descrição do Projeto - Academia Fitness

## Objetivo do Projeto

O objetivo deste projeto foi realizar uma análise de dados detalhada sobre o funcionamento da academia FITNES com foco em identificar uma oportunidade de negócio. Analisamos dados sobre frequência, atividades preferidas, horários de pico e taxas de cancelamento, e utilizamos esses insights para propor uma solução que pode otimizar a operação e aumentar a satisfação dos clientes.

## Oportunidade de Negócio

A análise de dados revelou diversas oportunidades, como a reorganização dos horários e a substituição de atividades de baixa adesão por opções mais populares. Além disso, identificamos que o plano básico é uma das principais causas de insatisfação e cancelamentos, sugerindo a necessidade de ajustes de preço e benefícios.

## Análises Realizadas

### Análise Temporal
- **Gráfico de Linha**: Observação de tendências de frequência ao longo do tempo.
- **Identificação de Sazonalidade**: Determinação de períodos mais e menos movimentados.

### Análise de Distribuição
- **Histograma/Boxplot**: Avaliação da distribuição de frequência e duração das atividades.
- **Outliers**: Identificação de picos de movimentação.

### Análise de Relacionamento
- **Gráfico de Dispersão/Heatmap**: Relação entre satisfação e adesão às modalidades, correlação entre motivos de cancelamento e frequência.
- **Padrões Significativos**: Correlação entre atividades e retenção de alunos.

### Análise Categórica
- **Gráfico de Barras/Pizza**: Comparação de popularidade entre modalidades e planos.
- **Identificação de Preferências**: Análise de popularidade por tipo de plano e atividade.

## Insights e Recomendações

1. **Otimização de Horários**: Reorganizar horários com baixa adesão para reduzir custos operacionais.
2. **Substituição de Modalidades**: Substituir atividades de baixa popularidade por outras mais procuradas, como Zumba e Yoga.
3. **Reformulação de Planos**: Ajuste no plano básico para melhorar a retenção de clientes, abordando os principais motivos de cancelamento.

## Ferramentas Utilizadas

- **Python** para análise de dados e geração de gráficos.
- **Bibliotecas**: Pandas, Matplotlib, Seaborn para visualização.
- **Streamlit** para criação do dashboard interativo.

## Dashboard Interativo

O dashboard desenvolvido permite que os investidores visualizem e explorem as análises de maneira dinâmica, incluindo:

- Frequência e sazonalidade.
- Análise de modalidades e cancelamentos.
- Gráficos categóricos para comparação entre planos e atividades.

---

## Conclusão e Próximos Passos

Com base nos dados e análises realizadas, sugerimos um investimento focado em otimização de recursos, substituição de modalidades e melhoria no plano básico. Acreditamos que essas mudanças aumentarão a retenção de clientes e otimizarão a operação, gerando um impacto positivo nos resultados da academia.

**Próximos Passos**:
- Implementar as mudanças sugeridas.
- Monitorar o impacto das alterações.
- Continuar a coleta e análise de dados para ajustes contínuos.

---

""")

# Informações do grupo
elif chart_type == "Informações do Grupo":
    st.markdown("<h1 style='text-align: center;'>Informações do grupo</h1>", unsafe_allow_html=True)
    st.markdown("********************")
    st.markdown("<h2 style='text-align: center;'>Integrantes do grupo FITNES</h2>", unsafe_allow_html=True)

    # Cria três colunas para exibir os integrantes
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(Funcoes.make_circle_image('src\\imgs\\Clarisse.jpg'), width=150)
        st.write('##### Clarisse Lima')
        st.write(' - Gravação do vídeo')
    with col2:
        st.image(Funcoes.make_circle_image('src\\imgs\\Malena.jpg'), width=150)
        st.write('##### Malena Milani')
        st.write(' - Repositório')
        st.write(' - Organização')
    with col3:
        st.image(Funcoes.make_circle_image('src\\imgs\\Isabela.jpg'), width=150)
        st.write('##### Isabela')
        st.write(' - Análise Categórica')
        st.write(' - Estilização')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(Funcoes.make_circle_image('src\\imgs\\Tiago.png'), width=150)
        st.write('##### Tiago Trindade')
        st.write(' - Criação do repositório')
        st.write(' - Análise Preditiva')
        st.write(' - Análise de relacionamento')
        st.write(' - Análise Temporal')
    with col2:
        st.image(Funcoes.make_circle_image('src\\imgs\\Pedro.jpg'), width=150)
        st.write('##### Pedro Neves')
        st.write(' - Análise de Distribuição')
        st.write(' - DashBoard')
        st.write(' - Estilização')
        st.write(' - Readme de descrição')
    with col3:
        st.image(Funcoes.make_circle_image('src\\imgs\\Max.jpg'), width=150)
        st.write('##### Max Clay')
        st.write(' - Revisões')

    col1, col2, col3 = st.columns(3)
    with col2:
        st.image(Funcoes.make_circle_image('src\\imgs\\Gustavo.jpg'), width=150)
        st.write('##### Gustavo Nascimento')
        st.write(' - Edições')

    st.markdown("********************")
    st.markdown("<h2 style='text-align: center;'>Descrição das Responsabilidades</h2>", unsafe_allow_html=True)
    st.markdown("""
## Código
### Tiago Trindade
- **Funções**: Criação do Repositório, Análise Preditiva, Análise de Relacionamento, Análise Temporal
- **Descrição**: Tiago contribuiu com análises complexas, avaliando tanto o comportamento passado quanto as possíveis tendências futuras. Ele focou nas interações dos clientes com a academia e no histórico temporal dos dados, além de realizar previsões de cenários futuros, o que possibilitou uma visão estratégica do projeto.

### Pedro Neves
- **Funções**: Análise de Distribuição, Dashboard, Estilização, Readme
- **Descrição**: Pedro liderou a análise de distribuição dos dados, sendo fundamental para identificar padrões de comportamento ao longo de diferentes períodos. Além disso, ele foi o responsável pela criação do dashboard, que apresentou as informações de forma interativa e acessível, facilitando a visualização dos dados pela equipe e pelos demais interessados. Pedro também se encarregou da estilização dos gráficos e relatórios.

### Isabela
- **Funções**: Análise Categórica, Estilização, Código
- **Descrição**: Isabela focou na análise categórica dos dados, identificando padrões qualitativos e destacando as categorias mais relevantes para o projeto. Ela também se encarregou da estilização dos gráficos e relatórios, garantindo que o material final fosse visualmente atraente e que comunicasse as informações de maneira clara e eficaz. Além disso, Isabela contribuiu com desenvolvimento de código.

## Documentação e Revisão
### Malena Milani
- **Funções**: Relatórios, Organização
- **Descrição**: Malena atuou na organização geral do projeto, mantendo os relatórios atualizados e estruturados. Sua atenção aos detalhes garantiu que todas as etapas fossem documentadas corretamente, permitindo um fluxo de trabalho mais eficiente e acesso fácil às informações para toda a equipe.

### Max Clay
- **Função Principal**: Revisões
- **Descrição**: Max foi o responsável por revisar todo o material desenvolvido pela equipe, incluindo tanto os códigos quanto os textos explicativos. Sua função foi essencial para garantir a clareza, consistência e coesão do conteúdo, assegurando que o material estivesse livre de erros e fosse compreensível para todos os usuários.

## Gravação e Edição
### Clarisse Lima
- **Função Principal**: Gravação do Vídeo
- **Descrição**: Clarisse foi responsável pela criação do material audiovisual da equipe. Sua tarefa envolveu sintetizar os principais pontos do trabalho em um vídeo coeso e envolvente. Além de narrar e organizar o conteúdo, ela trouxe um aspecto visual que facilitou a compreensão do projeto.

### Gustavo Nascimento
- **Funções**: Edições
- **Descrição**: Gustavo foi responsável pelas edições do material produzido pela equipe. Sua tarefa envolveu refinar e polir o conteúdo, garantindo a qualidade final dos produtos. Através de seu olhar crítico e atenção aos detalhes, Gustavo assegurou que o material fosse apresentado de forma coesa e impactante.
""")