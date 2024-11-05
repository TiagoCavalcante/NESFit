# Importando as bibliotecas nescessárias
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
df = pd.read_csv('C:\\Prog\\Py\\ProjetosPessoais\\Pratica_e_pesquisa\\NESFIT\\data\\fitness_gym.csv')


# Exibindo a imagem centralizada na barra lateral
Funcoes.display_centered_image('src/imgs/nesfitv2.jpg')
st.sidebar.image('src\\imgs\\satisfaction_stars.png')
chart_type = st.sidebar.selectbox("Navegação", ["Tela de Início","Mercado","Avaliações e Cancelamentos", "Estudo das atividades","Horários","Informações do Projeto", "Informações do Grupo"])


# Lógica para exibir os gráficos com base no seletor
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
# Página da Tela de Início
if chart_type == "Tela de Início":
    img_path = "src/imgs/Tela_Inicial.jpg"  # Substitua pelo caminho da sua imagem
    img_base64 = get_base64_of_bin_file(img_path)

    # CSS para aplicar o background com a imagem em base64
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

    # Injetando o CSS no Streamlit
    st.markdown(background_style, unsafe_allow_html=True)



# Página do Mercado
elif chart_type == "Mercado":

    # Duas colunas para o contexto de Mercado
    col1, col2 = st.columns(2)
    with col1:
        # Adicona imagem a primeira coluna
        st.image('src\\imgs\\gym_mercado.png')
    with col2:
        # Adiciona o texto de contexto de mercado à segunda coluna
        st.markdown("<h1 style='text-align: center;'>Contexto de mercado</h1>", unsafe_allow_html=True)
        st.markdown("""
                    ***********************
#### -O mercado fitness é uma área ampla que contempla negócios voltados à saúde e bem-estar de modo geral.
                    
#### -Durante as últimas décadas, a necessidade de exercícios físicos é cada vez maior, a crescente preocupação com a saúde fez com que mais pessoas procurassem academias e espaços fitness.



                    """) 

    st.markdown("""************************""")

    # Duas colunas para as estatísticas de mercado    
    col1, col2 = st.columns(2)
    with col1:
        # Adiciona o texto das estatísticas de mercado à primeira coluna
        st.markdown("<h1 style='text-align: center;'>Estatísticas do mercado</h1>", unsafe_allow_html=True)
        st.markdown("""

*******************
#### -O mercado fitness no Brasil fatura R$ 12 bilhões ao ano, de acordo com o Panorama Setorial de 2023.   

#### -O valor transacionado com academias e produtos fitness cresceu cerca de 35% em 2023 comparado ao ano anterior, segundo estudo do Itaú Unibanco.

""")
        
         
    with col2: 
        # Adiciona a imagem a segunda coluna
        st.image('src\\imgs\\gym_mercado2.png')

#Avaliações e Cancelamentos        
elif chart_type == "Avaliações e Cancelamentos":
    st.markdown("<h1 style='text-align: center;'>Avaliações e Cancelamentos</h1>", unsafe_allow_html=True)
    st.pyplot(Funcoes.cancelamento_plano(df))
    st.markdown("""

## Principais motivos de cancelamento:
    
#### Insatisfação: 40% 
#### Custo alto: 25%
#### Falta de tempo: 20%


## Cancelamentos por plano:               
### Basic: 80%
#### Principais motivos:
##### -Insatisfação
##### -Custo alto
                
### Premium: 20%
#### Principais motivos:
##### -Falta de tempo
##### -Custo alto


*********************
""")
    

    st.write("<h1 style='text-align: center;'>Satisfação média por plano</h1>", unsafe_allow_html=True)
    
    st.pyplot(Funcoes.satisfacao_plano(df))

    st.markdown("""
                
### Observação:
#### Classificação do plano básico está bem abaixo dos outros.


************************
""")

    st.write("<h1 style='text-align: center;'>Problemas e soluções</h1>", unsafe_allow_html=True)
    st.markdown("""
    
    ## Problemas:
    ### - Altas taxas de cancelamento no plano Basic.
    ### - Altos indices insatisfação no plano Basic.
    ### - Muitas reclamações sobre preços altos nos planos Basic e Premium.

    ## Em geral:
    #### Está perdendo muitos cliente devido a baixa qualidade e alto valor do plano Basic.
    
    
    ## Solução:
    #### - Investigar como o plano Basic pode ser melhorado para atender melhor aos clientes.
    #### - Repensar o preço do plano Basic para se encaixar melhor no orçamentos dos clientes.
    """)



#Horários

elif chart_type == "Horários":
    st.markdown("<h1 style='text-align: center;'>Horários</h1>", unsafe_allow_html=True)
    st.write("## Frequencia diária dos alunos")
    st.pyplot(Funcoes.frequencia_dia(df))
    st.markdown("""

                







****************
""")


 #Informações do projeto
elif chart_type == "Informações do Projeto":
    st.markdown("<h1 style='text-align: center;'>Informações do projeto</h1>", unsafe_allow_html=True)
    st.markdown("********************")
    st.write('## Objetivo')
    st.write('###### - Desenvolver uma plataforma digital que facilite a gestão e avaliação dos plano de academia do G2 NESFIT.')
    st.write('## Metas')
    st.write('###### - Aumentar a taxa de cancelamento de clientes.')
    st.write('###### - Melhorar a qualidade do serviço.')
    st.write('###### - Aumentar a satisfação dos clientes.')
    st.write('## Estratégia')
    st.write('###### - Utilizar dados de clientes e avaliações para melhorar o plano de')

#Informações do grupo
elif chart_type == "Informações do Grupo":
    st.markdown("<h1 style='text-align: center;'>Informações do projeto</h1>", unsafe_allow_html=True)
    st.markdown("********************")
    st.write('## Integrantes do Grupo NESFIT')
    
    col1, col2,col3 = st.columns(3)
    with col1:
        st.image(Funcoes.make_circle_image('src\\imgs\\Clarisse.jpg'),width= 150)
        st.write('##### Clarisse Lima')
        st.write('###### -Gravação do vídeo')
    with col2:
        st.image(Funcoes.make_circle_image('src\\imgs\\Pedro.jpg'),width= 150)
        st.write('##### Pedro Neves')
        st.write('###### -Análise de Distribuição')
        st.write('###### -DashBoard')
    with col3:
        st.image(Funcoes.make_circle_image('src\\imgs\\Malena.jpg'),width= 150)
        st.write('##### Malena Milani')
        st.write('###### -Repositório')
        st.write('###### -Organização')

    col1, col2,col3 = st.columns(3)
    with col1:
        st.image(Funcoes.make_circle_image('src\\imgs\\Tiago.png'),width= 150)
        st.write('##### Tiago Trindade')
        st.write('###### -Criação do repositório')
        st.write('###### -Análise Preditiva')
        st.write('###### -Análise de relacionamento')
        st.write('###### -Análise Temporal')
        
    with col2:
        st.image(Funcoes.make_circle_image('src\\imgs\\Max.jpg'),width= 150)
        st.write('##### Max Clay')
        st.write('###### -Revisões')
    with col3:
        st.image(Funcoes.make_circle_image('src\\imgs\\Malena.jpg'),width= 150)
        st.write('##### Isabela')
        st.write('###### -Análise Categórica')
        st.write('###### -Estilização')
    col1, col2,col3 = st.columns(3)
    with col2:
        st.image(Funcoes.make_circle_image('src\\imgs\\Gustavo.jpg'),width= 150)
        st.write('##### Gustavo Nascimento')
        st.write('###### -Edições')
    st.markdown("********************")
    st.markdown("""                
### Descrição Detalhada:

#### -Pedro Henrique Vasconcelos Neves (Mód. II):
##### Tempo dedicado: 17hrs 12 min
##### Tarefas:
###### -Análise de distribuição (Arquivo Analise_Distribuicao.ipynb)
###### -Criação e estilização do Dashboard (Arquivo Dashboard.py)
###### -Criacão das funções (Arquivo Functions.py)

                

                
    """)

    
#Análise de distribuição
elif chart_type == "Estudo das atividades":
    st.write('# Estudo das atividades da academia')
    st.write("### Atividades mais realizadas")
    st.pyplot(Funcoes.distribuicao_atividades(df))
    import streamlit as st

    st.markdown("""
    ### Top 3 atividades mais realizadas:
    #### 1. Zumba
    #### 2. Yoga
    #### 3. Musculação
    *******************************    
    """)

    st.write("### Calorias X Atividades")
    st.write("#### Média de calorias queimadas por atividade")
    st.pyplot(Funcoes.calorias_atividade(df))

    st.markdown("""
    ### Top 3 atividades com mais calorias queimadas:
    #### 1. CrossFit
    #### 2. Spinning
    #### 3. Boxing
    
    *******************************    

    """)


    st.write("## Distribuição das Idades dos participantes")
    st.pyplot(Funcoes.distribuicao_idades(df))

    st.markdown("""
    #### Idade Média do participantes: 42 Anos
    #### Idade Mínima encontrada: 18 anos
    #### Idade Máxima encontrada: 64 anos

    *******************************                
    """)

    st.write('## Categoria das atividades')
    st.pyplot(Funcoes.activity_category(df))

    st.markdown("""
    ### Principais categorias:
    #### 1. Bem estar
    #### 2. Dança
    #### 3. Força
    """)
    
    st.write("<h1 style='text-align: center;'>Problemas e soluções</h1>", unsafe_allow_html=True)
    st.markdown("""
    
    ## Problemas:
    ### - A atividade Jump tem poucos participantes.
    ### - A ativide Jump queima poucas calorias.
    ### - A atividade Jump não se enquadra com o público da academia.

    ## Em geral:
    #### A atividade Jump não está sendo lucrativa o suficiente e fora do padrão do público da academia.
    
    
    ## Solução:
    #### - Analisar como é possível substituir a atividade Jump por outra que se encaixe mais ao nosso público, como Zumba ou Yoga.
    #### - Repensar o preço do plano Basic para se encaixar melhor no orçamentos dos clientes.
    """)
    



        
    