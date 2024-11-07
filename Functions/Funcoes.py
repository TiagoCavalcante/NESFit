import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
from PIL import Image, ImageDraw
import base64
from io import BytesIO

# Função para converter imagem em base64 para HTML
def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

#Funnção para centralizar imagem
def centralize_image(image_path, width=None):
    image_html = f"""
        <div style="display: flex; justify-content: center;">
            <img src="{image_path}" style="{'width: ' + str(width) + 'px;' if width else ''}">
        </div>
    """
    st.sidebar.markdown(image_html, unsafe_allow_html=True)


# Função para exibir a imagem centralizada
def display_centered_image(image_path):
    img = make_circle_image(image_path)
    img_base64 = image_to_base64(img)
    img_html = f"""
        <div style="display: flex; justify-content: center;">
            <img src="data:image/png;base64,{img_base64}" style="border-radius: 50%; width: 150px;">
        </div>
    """
    st.sidebar.markdown(img_html, unsafe_allow_html=True)


#Função para arrendondar imagem
def make_circle_image(image_path):
    img = Image.open(image_path).convert("RGBA")
    bigsize = (img.size[0] * 3, img.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(img.size, Image.LANCZOS)
    img.putalpha(mask)
    return img




def distribuicao_atividades(df):#Grafico de distribuição das ativades 

#Seleciona a coluna activity do dataframe df, que contém informações sobre os tipos de atividades praticadas na academia.
    activity = df.groupby('activity')['activity'].count().reset_index(name="Quantidade")
    activity.sort_values(by='Quantidade', ascending=False, inplace=True)


    #Configura o tamanho da figura e define uma cor para a área externa da figura.
    plt.figure(figsize=(10,5), facecolor = '#0A0D0F')

    #Criando um histograma com as atividades praticadas na academia.
    plt.bar( x= activity['activity'], height = activity['Quantidade'],color = '#0A2538')

    #Alterando a cor de fundo do gráfico.
    plt.gca().set_facecolor('#E2CC9C')


    #Adiciona e personaliza a grade do gráfico.
    plt.grid(True,color = '#0A2538', linestyle = "--", alpha = 0.7)

    #Adicionando um título ao gráfico, define a cor do título e o tamanho do título.
    plt.title('Distribuição das atividades na academia', fontsize=16, color='#E64B2D')

    #Labels e ticks.
    plt.xlabel('Atividades', fontsize=14, color='#E64B2D')
    plt.ylabel('Frequência', fontsize=14, color='#E64B2D')
    plt.xticks(color ='#E2CC9C',fontsize=10)
    plt.yticks(color ='#E2CC9C',fontsize=10)

    #Apresenta o gráfico.
    return plt

def distribuicao_idades(df):
    # Pegando as idades
    ages = df['age']

    # Configura o tamanho da figura e define uma cor para a área externa da figura.
    plt.figure(figsize=(10, 5), facecolor='#0A0D0F')

    # Criando um histograma com as idades
    plt.hist(ages, bins=20, color='#E64B2D', edgecolor='black', alpha=0.7, density= True)

    # Alterando a cor de fundo do gráfico.
    plt.gca().set_facecolor('#E2CC9C')

    # Adicionando e estilizando a grade
    plt.grid(True, color='#0A2538', alpha=0.7, linestyle='--')

    # Adicionando um título ao gráfico, define a cor do título e o tamanho do título.
    plt.title('Distribuição das idades na academia', color='#E2CC9C', fontsize=16)

    # Labels e ticks
    plt.xlabel('Idade', color='#E2CC9C', fontsize=14)
    plt.ylabel('Densidade', color='#E2CC9C', fontsize=14)
    plt.xticks(color='#E2CC9C', fontsize=10)
    plt.yticks(color='#E2CC9C', fontsize=10)

    # Criando uma linha de densidade (KDE)
    sns.kdeplot(ages, color='#0A2538', linewidth=2, label='Densidade')

    plt.legend()

    return plt



def calorias_atividade(df):
    #Agrupa a coluna activity com uma coluna formada pela média de calorias queimadas em cada atividade
    calorias_atividade = df.groupby('activity')['calories_burned'].mean().reset_index()

    #Ordena a coluna pela média de calorias queimadas em ordem decrescente
    calorias_atividade.sort_values(by='calories_burned', ascending=False, inplace=True)

    #Configura o tamanho da figura e define uma cor para a área externa da figura.
    plt.figure(figsize=(10,5), facecolor = '#0A0D0F')
    #Cria um gráfico de barras com a média de calorias queimadas por atividade na academia.
    plt.bar(x=  calorias_atividade['activity'], height = calorias_atividade['calories_burned'],color = '#0A2538')

    #Alterando a cor de fundo do gráfico.
    plt.gca().set_facecolor('#E2CC9C')

    #Adicionando e estilizando a grade
    plt.grid(True,color = '#0A2538', linestyle = "--", alpha = 0.7)

    #Adicionando um título ao gráfico, define a cor do título e o tamanho do título.
    plt.title('Media de calorias queimadas por atividade', fontsize=16, color='#E64B2D')

    #Labels e ticks.
    plt.xlabel('Atividades', fontsize=14, color='#E64B2D')
    plt.ylabel('Média de calorias queimadas', fontsize=14, color='#E64B2D')
    plt.xticks(color ='#E2CC9C',fontsize=10)
    plt.yticks(color ='#E2CC9C',fontsize=10)

    #Mostra o gráfico.
    return plt



def satisfacao_plano(df):
    # Calculando a média de satisfação para cada tipo de plano
    media_satisfacao = df.groupby("membership_type")["satisfaction_score"].mean()

    # Definido o tamanaho do gráfico
    plt.figure(figsize=(10, 6), facecolor='#0A2538')

    # plotando o gráfico
    plt.plot(media_satisfacao.index, media_satisfacao.values, marker='o', color="#E84A2E", linewidth=2)

    # Definindo a aparência do gráfico
    plt.title("Média de Satisfação por Tipo de Plano", color="#E84A2E", fontsize=14)
    plt.xlabel("Tipo de Plano", color="#E84A2E", fontsize=12)
    plt.ylabel("Média de Satisfação (1 a 5)", color="#E84A2E", fontsize=12)
    plt.xticks(color='#E84A3E')
    plt.yticks(color='#E84A3E')
    plt.gca().set_facecolor('#E2E4E7')
    plt.grid(True)

    # Apresentando o gráfico
    return plt

def cancelamento_plano(df):
    # Tamanho e cor da figura
    plt.figure(figsize=(12, 6), facecolor='#E84A2E')

    # Paleta de cores das barras
    colors = ['#A4B8C4', '#BF5B32', '#E84A2E', '#0A2538', '#E2CC9C']

    # Plotando o gráfico com seaborn por permitir a melhor organização dos dados
    sns.countplot(data=df, x="membership_type", hue="cancellation_reason", palette=colors)

    # Customização
    plt.title("Motivo de Cancelamento por Tipo de Plano", fontsize=16)
    plt.xlabel("Tipo de Plano", fontsize=14)
    plt.ylabel("Quantidade", fontsize=14)
    plt.legend(title="Motivo de Cancelamento")
    plt.grid(True)

    return plt

# Função que centraliza uma imagem usando HTML no Streamlit



def plano_categoria(df):
    colors = ['#0A2538', '#BF5B32', '#E84A2E' , '#E2CC9C']
    df_activity_category_membership_type = df.groupby(['activity_category','membership_type'])['membership_type'].count().reset_index(name='membership_count')
    plt.figure(figsize=(12, 6), facecolor= '#0A0D0F')
    sns.barplot(data=df_activity_category_membership_type, x='activity_category', y='membership_count', hue='membership_type', palette=colors)

    plt.grid(True, color ='#0A0D0F', linestyle='--')

    plt.gca().set_facecolor('#E2CC9C')

    # Add title and labels
    plt.title('Quantidade de mebros por plano em cada Categoria de atividade',color= '#E84A2E',fontsize = 16)
    plt.xlabel('Categoria da Atividade',color= '#E84A2E', fontsize = 14)
    plt.ylabel('Quantidade de Alunos',color= '#E84A2E', fontsize =14)

    # Display the legend
    plt.legend(title='Tipo de Mmenbro')
    return plt


def activity_category(df):
    colors = ['#0A2538', '#BF5B32', '#E84A2E' , '#E2CC9C']
    df_activity_category_membership_type = df.groupby(['activity_category','membership_type'])['membership_type'].count().reset_index(name='membership_count')
    plt.figure(figsize=(12, 6), facecolor= '#0A0D0F')
    sns.barplot(data=df_activity_category_membership_type, x='activity_category', y='membership_count', hue='membership_type', palette=colors)

    plt.grid(True, color ='#0A0D0F', linestyle='--')

    plt.gca().set_facecolor('#E2CC9C')

    # Add title and labels
    plt.title('Alunos por categoria de atividade e tipo de membro',color= '#E84A2E',fontsize = 16)
    plt.xlabel('Categoria de atividade',color= '#E84A2E', fontsize = 14)
    plt.ylabel('Quantidade de Alunos',color= '#E84A2E', fontsize =14)
    plt.xticks(color ='#E2CC9C',fontsize=10)
    plt.yticks(color ='#E2CC9C',fontsize=10)

    # Display the legend
    plt.legend(title='Membership Type')
    return plt
    


def frequencia_dia(df):
    # Converter a coluna de time para formato datetime
    df["time"] = pd.to_datetime(
    df["time"], format="%H:%M:%S"
    ).dt.hour

    # Agrupar por horário
    hourly_pattern = df.groupby("time").size()

    # Plotando gráfico de barras para o padrão por horário
    plt.figure(figsize=(10, 6), facecolor='#151515')
    plt.bar(
    hourly_pattern.index, hourly_pattern.values, color='#BF5B32',
    linewidth=0.6, edgecolor='black'
    )
    plt.gca().set_facecolor('#E2CC9C')
    plt.title("Frequência por Horário do Dia", color='#E2CC9C', fontsize=16)
    plt.xlabel("Hora", color='#E2CC9C', fontsize=14)
    plt.ylabel("Número de Check-ins", color='#E2CC9C', fontsize=14)
    plt.xticks(color='#E2CC9C', fontsize=10)
    plt.yticks(color='#E2CC9C', fontsize=10)
    plt.grid(True, color='gray')
    return plt


def frequencia_mes(df):
    # Criando coluna com o mês
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.month

    # Agrupando por mês
    monthly_pattern = df.groupby("month").size()

    # Plotando gráfico de barras para o padrão mensal
    plt.figure(figsize=(10, 6), facecolor='#151515')
    plt.bar(
    monthly_pattern.index, monthly_pattern.values, color='#BF5B32'
    )
    plt.gca().set_facecolor('#E2CC9C')
    plt.title("Frequência Mensal dos Alunos", fontsize=16, color='#E2CC9C')
    plt.xlabel("Mês", fontsize=14, color='#E2CC9C')
    plt.ylabel("Número de Check-ins", fontsize=14, color='#E2CC9C')
    plt.xticks(color='#E2CC9C',fontsize=10)
    plt.yticks(color='#E2CC9C',fontsize=10)
    plt.grid(True, color='gray')
    return plt



import matplotlib.pyplot as plt

def distribuicao_assinaturas(df):
    # Contagem dos tipos de assinatura
    membership_counts = df["membership_type"].value_counts()
    
    # Configurações do gráfico
    plt.figure(figsize=(6, 6), facecolor='#0E1117')
    plt.rcParams.update({'font.size': 12, 'font.family': 'Arial'})

    # Criando o gráfico de pizza com Matplotlib
    wedges, texts, autotexts = plt.pie(
        membership_counts,
        labels=membership_counts.index,
        autopct="%1.1f%%",
        colors=['#E84A2E', '#E2CC9C', '#A4B8C4'],
        wedgeprops={'edgecolor': 'white', 'linewidth': 1.5},
        startangle=140
    )

    # Configuração dos textos e rótulos
    for text in texts:
        text.set_color("#E84A2E")  # Define a cor "#E84A2E" para os nomes dos planos
    
    for autotext in autotexts:
        autotext.set_color("Black")  # Define o texto do percentual em branco
        autotext.set_fontsize(14)
        autotext.set_weight("bold")

    # Título do gráfico
    plt.title("Distribuição dos Tipos de Assinatura", fontsize=16, color="#E84A2E", weight="bold")
    
    # Adicionar legenda com nomes dos planos
    plt.legend(
        membership_counts.index, 
        title="Tipos de Assinatura", 
        loc="upper right",
        bbox_to_anchor=(1.2, 1),
        title_fontsize=12,
        fontsize=10,
        labelcolor="Black"  # Define a cor da legenda para "#E84A2E"
    )

    # Exibir o gráfico
    return plt

