#Importando as bibliotecas nescessárias
from Functions import Funcoes_Distribuicao
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
import numpy as np
import streamlit as st 

df = pd.read_csv('C:\\Prog\\Py\\ProjetosPessoais\\Pratica_e_pesquisa\\NESFIT\\data\\fitness_gym.csv')

# Seletor de gráficos no painel lateral
from PIL import Image, ImageDraw

from PIL import Image, ImageDraw, ImageOps

#imagem da side bar
def make_circle_image(image_path, size=(100, 100)):
    try:
        # Open the image
        image = Image.open(image_path)

        # Resize the image
        image = image.resize(size, Image.LANCZOS)

        # Create a mask to make the image circular
        mask = Image.new('L', size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size[0], size[1]), fill=255)

        # Create a circular cropped image
        circular_image = ImageOps.fit(image, mask.size, Image.LANCZOS)
        circular_image.putalpha(mask)

        return circular_image
    except Exception as e:
        print(f"Error processing image: {e}")
        return None  # Return None if there's an error

st.sidebar.image(make_circle_image('src\\imgs\\nesfitv2.jpg.webp'))

chart_type = st.sidebar.selectbox("Navegação", ["Tela de Início","Mercado", "Análises de Distribuição", "Informações do Grupo"])

# Lógica para exibir os gráficos com base no seletor

if chart_type == "Tela de Início":
    st.markdown("<h1 style='text-align: center;'>G2 NESFIT</h1>", unsafe_allow_html=True)
    st.image('src\\imgs\\Tela Inicial.png')

elif chart_type == "Mercado":
    col1, col2 = st.columns(2)
    with col1:
        st.image('src\\imgs\\gym_mercado.png')
    with col2:
        st.markdown("<h1 style='text-align: center;'>Contexto de mercado</h1>", unsafe_allow_html=True)
        st.markdown("""
                    ***********************
#### -O mercado fitness é uma área ampla que contempla negócios voltados à saúde e bem-estar de modo geral.
                    
#### -Durante as últimas décadas, a necessidade de exercícios físicos é cada vez maior, a crescente preocupação com a saúde fez com que mais pessoas procurassem academias e espaços fitness.



                    """) 

    st.markdown("""************************""")     
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h1 style='text-align: center;'>Estatísticas do mercado</h1>", unsafe_allow_html=True)
        st.markdown("""

*******************
#### -O mercado fitness no Brasil fatura R$ 12 bilhões ao ano, de acordo com o Panorama Setorial de 2023   

#### -O valor transacionado com academias e produtos fitness cresceu cerca de 35% em 2023 comparado ao ano anterior, segundo estudo do Itaú Unibanco

""")
        
         
    with col2: 
        st.image('src\\imgs\\gym_mercado2.png')

elif chart_type == "Informações do Grupo":
    st.markdown("<h1 style='text-align: center;'>Informações do projeto</h1>", unsafe_allow_html=True)
    st.markdown("********************")
    st.write('## Integrantes do Grupo NESFIT')
    
    col1, col2,col3 = st.columns(3)
    with col1:
        st.image(make_circle_image('src\\imgs\\Clarisse.jpg'))
        st.write('###### Clarisse Lima')
        st.write('###### -Gravação do vídeo')
    with col2:
        st.image(make_circle_image('src\\imgs\\Pedro.jpg'))
        st.write('###### Pedro Neves')
        st.write('###### -Análise de Distribuição')
        st.write('###### -DashBoard')
    with col3:
        st.image(make_circle_image('src\\imgs\\Malena.jpg'))
        st.write('###### Malena Milani')
        st.write('###### -Repositório')
        st.write('###### -Organização')

    col1, col2,col3 = st.columns(3)
    with col1:
        st.image(make_circle_image('src\\imgs\\Tiago.png'))
        st.write('###### Tiago')
        st.write('###### -Análise de relacionamento')
        st.write('###### -Análise Temporal')
    with col2:
        st.image(make_circle_image('src\\imgs\\Gustavo.jpg'))
        st.write('###### Gustavo')
        st.write('###### -Edição de vídeo')
    with col3:
        st.image(make_circle_image('src\\imgs\\Malena.jpg'))
        st.write('###### Malena Milani')
        st.write('###### -Repositório')
        st.write('###### -Organização')
    st.markdown("********************")
    st.markdown("""                
### Descrição do papel do integrantes:

                
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.








    """)

elif chart_type == "Análises de Distribuição":
    st.write('# Analise de distribuição')
    st.write("### Distribuição das atividades")
    st.pyplot(Funcoes_Distribuicao.Distribuicao_Atividades(df))
    import streamlit as st

    st.markdown("""
    ### Top 3 atividades mais realizadas:
    #### 1. Zumba
    #### 2. Yoga
    #### 3. Musculação


    #### Observações:
    Aqui vai ser adicionada alguma descrição bonitinha ou algumas oportunidade de negocio descoberta a partir do grafico. Agora estou só enchendo linguiça pra ficar bonitinho.
    """)

    st.write("### Calorias X Atividades")
    st.write("#### Média de calorias queimadas por atividade")
    st.pyplot(Funcoes_Distribuicao.Calorias_Atividade(df))

    st.markdown("""
    ### Top 3 atividades com mais calorias queimadas:
    #### 1. Zumba
    #### 2. Yoga
    #### 3. Musculação


    #### Observações:
    Aqui vai ser adicionada alguma descrição bonitinha ou algumas oportunidade de negocio descoberta a partir do grafico. Agora estou só enchendo linguiça pra ficar bonitinho.
    """)


    st.write("#### Distribuição das idades")
    st.pyplot(Funcoes_Distribuicao.Distribuicao_Idades(df))

    st.markdown("""
    #### Idade Média do participantes: 42 Anos
    #### Idade Mínima encontrada: 18 anos
    #### Idade Máxima encontrada: 64 anos

                    
    #### Observações:
    Em média a academia possui mais participantes em idades proximas a 40 anos que participam de atividades mas focadas em Mobilidade, força e vitalidade. Atividades como Jump, Boxe tem ficado para trás, isso pode ser resolvido tornando a academia mais atrante ao público jovem.
    """)



        
    