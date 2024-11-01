import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
import numpy as np
import streamlit as st 
def Distribuicao_Atividades(df):#Grafico de distribuição das ativades 

#Seleciona a coluna activity do dataframe df, que contém informações sobre os tipos de atividades praticadas na academia.
    activity = df['activity']

    #Configura o tamanho da figura e define uma cor para a área externa da figura.
    plt.figure(figsize=(10,5), facecolor = '#0A0D0F')

    #Criando um histograma com as atividades praticadas na academia.
    plt.hist(activity,color='#0A2538',bins=15)

    #Alterando a cor de fundo do gráfico.
    plt.gca().set_facecolor('#E2CC9C')


    #Adiciona e personaliza a grade do gráfico.
    plt.grid(True,color = '#0A2538', linestyle = "--", alpha = 0.7)

    #Adicionando um título ao gráfico, define a cor do título e o tamanho do título.
    plt.title('Distribuição das atividades na academia', fontsize=16, color='#E64B2D')

    #Labels e ticks.
    plt.xlabel('Activity', fontsize=14, color='#E64B2D')
    plt.ylabel('Frequency', fontsize=14, color='#E64B2D')
    plt.xticks(color ='#E2CC9C',fontsize=10)
    plt.yticks(color ='#E2CC9C',fontsize=10)

    #Apresenta o gráfico.
    return plt

def Distribuicao_Idades(df):
    #Pegando as idades
    ages = df['age']


    #Configura o tamanho da figura e define uma cor para a área externa da figura.
    plt.figure(figsize=(10,5), facecolor='#0A0D0F')

    #Criando um histograma com as idades
    plt.hist(ages,bins=20,color='#E64B2D')

    #Alterando a cor de fundo do gráfico.
    plt.gca().set_facecolor('#E2CC9C')

    #Adicionando e estilizando a grade
    plt.grid(True,color='#0A2538',alpha = 0.7, linestyle='--')

    #Adicionando um título ao gráfico, define a cor do título e o tamanho do título.
    plt.title('Distribuição das idade na academia', color='#E2CC9C',fontsize=16)

    #Labels e ticks.
    plt.xlabel('Age',color='#E2CC9C',fontsize=14)
    plt.ylabel('Count',color='#E2CC9C',fontsize=14)
    plt.xticks(color ='#E2CC9C',fontsize=10)
    plt.yticks(color ='#E2CC9C',fontsize=10)



    #Criando um gráfico em linha
    age_counts, bin_edges = np.histogram(ages, bins=20)
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    plt.plot(bin_centers, age_counts, color='#0A2538', marker='o', linestyle='-', linewidth=2, label='Linha')

    return plt


def Calorias_Atividade(df):
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

