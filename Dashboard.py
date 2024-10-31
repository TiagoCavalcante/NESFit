#Importando as bibliotecas nescessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
import numpy as np
import streamlit as st 

df = pd.read_csv('C:\\Prog\\Py\\ProjetosPessoais\\Pratica_e_pesquisa\\NESFIT\\data\\fitness_gym.csv')

def Distribuicao_Atividades(df):#Grafico de distribuição das ativades 

    plt.figure(figsize=(10,5), facecolor = '#0A0D0F')
    plt.grid(True,color = '#0A2538', linestyle = "--", alpha = 0.7)
    plt.title('Distribution of Activities in the Gym', fontsize=16, color='#E64B2D')
    plt.xlabel('Activity', fontsize=14, color='#E64B2D')
    plt.ylabel('Frequency', fontsize=14, color='#E64B2D')
    plt.xticks(color ='#E2CC9C',fontsize=10)
    plt.yticks(color ='#E2CC9C',fontsize=10)
    plt.hist(df['activity'],color='#0A2538',bins=15)
    plt.gca().set_facecolor('#E2CC9C')
    return plt
def Distribuicao_Idades(df):
#Pegando as idades
    ages = df['age']


    #definindo a figure
    plt.figure(figsize=(10,5), facecolor='#0A0D0F')

    #Criando um histograma com as idades
    plt.hist(ages,bins=20,color='#E64B2D')

    #Adicionando e estilizando a grade
    plt.grid(True,color='#0A2538',alpha = 0.7, linestyle='--')

    #Titulos, labels e ticks
    plt.title('Distribuition of ages in the GYM', color='#E2CC9C',fontsize=16)
    plt.xlabel('Age',color='#E2CC9C',fontsize=14)
    plt.ylabel('Count',color='#E2CC9C',fontsize=14)
    plt.xticks(color ='#E2CC9C',fontsize=10)
    plt.yticks(color ='#E2CC9C',fontsize=10)

    #background color
    plt.gca().set_facecolor('#E2CC9C')

    #Criando um gráfico em linha
    age_counts, bin_edges = np.histogram(ages, bins=20)
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    plt.plot(bin_centers, age_counts, color='#0A2538', marker='o', linestyle='-', linewidth=2, label='Linha')
    return plt



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

chart_type = st.sidebar.selectbox("Navegação", ["Tela de Início", "Informações do Projeto", "Análises de Distribuição"])

# Lógica para exibir os gráficos com base no seletor

if chart_type == "Tela de Início":
    st.markdown("<h1 style='text-align: center;'>G2 NESFIT</h1>", unsafe_allow_html=True)
    st.image('src\\imgs\\Tela Inicial.png')
    

elif chart_type == "Informações do Projeto":
    st.markdown("<h1 style='text-align: center;'>Informações do projeto</h1>", unsafe_allow_html=True)
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
    st.markdown("""                
### Descrição do Projeto:

Projeto focado na análise dos dados da academia para identificar padrões, relações e oportunidades de desenvolcimento e aprimoramento da academia.






    """)

elif chart_type == "Análises de Distribuição":
    st.write('# Analise de distribuição')
    st.write("### Distribuição das atividades")
    st.pyplot(Distribuicao_Atividades(df))
    import streamlit as st

    st.markdown("""
    ### Top 3 atividades mais realizadas:
    #### 1. Zumba
    #### 2. Yoga
    #### 3. Musculação


    #### Observações:
    Aqui vai ser adicionada algumas descrição bonitinha ou algumas oportunidade de negocio descoberta a partir do grafico. Agora estou só enchendo linguiça pra ficar bonitinho.
    """)

    
    st.write("#### Distribuição das idades")
    st.pyplot(Distribuicao_Idades(df))

    st.markdown("""
    #### Idade Média do participantes: 42 Anos
    #### Idade Mínima encontrada: 18 anos
    #### Idade Máxima encontrada: 64 anos

                    
    #### Observações:
    Em média a academia possui mais participantes em idades proximas a 40 anos que participam de atividades mas focadas em Mobilidade, força e vitalidade. Atividades como Jump, Boxe tem ficado para trás, isso pode ser resolvido tornando a academia mais atrante ao público jovem.
    """)



        
    