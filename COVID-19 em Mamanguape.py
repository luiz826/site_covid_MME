#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 00:31:37 2021

@author: luizf
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("https://raw.githubusercontent.com/luiz826/site_covid_MME/main/mme.csv")
df["data"] = pd.to_datetime(df["data"],dayfirst=True)
df.set_index("data",inplace=True)
df.columns = ["Casos Confirmados Acumulados", "Óbitos Confirmados Acumulados", "Casos Confirmados por Notificação", "Óbitos Confirmados por Notificação"]

med_casos = df["Casos Confirmados por Notificação"].mean()
med_obt = df["Óbitos Confirmados por Notificação"].mean()
max_casos = df["Casos Confirmados por Notificação"].max()
max_obt = df["Óbitos Confirmados por Notificação"].max()

# GRAFICOS

fig = go.Figure()
        
fig.add_trace(go.Scatter(x=df.index,
                        y=df["Casos Confirmados Acumulados"].values,
                        mode="lines",
                        line=dict(color='steelblue', width=3),
                        fill='tozeroy'))

fig.update_layout(template="simple_white",
                  font_family='Rockwell',width=800, height=500)

fig.update_xaxes(tickangle = -30,
                title_text = "",
                title_font = {"size": 50},
                title_standoff = 15,
                showline=True,
                 linewidth=4,
                 linecolor='lightgrey')

fig2 = go.Figure()
        
fig2.add_trace(go.Scatter(x=df.index,
                        y=df["Casos Confirmados por Notificação"].values,
                        mode="lines",
                        line=dict(color='steelblue', width=3),
                        fill='tozeroy'))

fig2.update_layout(template="simple_white", 
                  font_family='Rockwell',width=800, height=500)

fig2.update_xaxes(tickangle = -30,
                title_text = "",
                title_font = {"size": 50},
                title_standoff = 15,
                showline=True,
                 linewidth=4,
                 linecolor='lightgrey')

fig3 = go.Figure()
        
fig3.add_trace(go.Scatter(x=df.index,
                        y=df["Óbitos Confirmados Acumulados"].values,
                        mode="lines",
                        line=dict(color='tomato', width=3),
                        fill='tozeroy'))

fig3.update_layout(template="simple_white", 
                  font_family='Rockwell',width=800, height=500)

fig3.update_xaxes(tickangle = -30,
                title_text = "",
                title_font = {"size": 50},
                title_standoff = 15,
                showline=True,
                 linewidth=4,
                 linecolor='lightgrey')

fig4 = go.Figure()
        
fig4.add_trace(go.Scatter(x=df.index,
                        y=df["Óbitos Confirmados por Notificação"].values,
                        mode="lines",
                        line=dict(color='tomato', width=3),
                        fill='tozeroy'))

fig4.update_layout(template="simple_white", 
                  font_family='Rockwell',width=800, height=500)

fig4.update_xaxes(tickangle = -30,
                title_text = "",
                title_font = {"size": 50},
                title_standoff = 15,
                showline=True,
                 linewidth=4,
                 linecolor='lightgrey')

fig5 = go.Figure()

fig5.add_trace(go.Histogram(
    x=df["Óbitos Confirmados por Notificação"],
    bingroup=30, marker_color="tomato"))
fig5.update_layout(template="simple_white",
                  font_family='Rockwell',width=800, height=500,)


fig6 = go.Figure()

fig6.add_trace(go.Histogram(
    x=df["Casos Confirmados por Notificação"],
    bingroup=30, marker_color="steelblue"))
fig6.update_layout(template="simple_white",
                  font_family='Rockwell',width=800, height=500,)



# APP

st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/6/64/Brasaomamanguape.png", use_column_width=True)
st.sidebar.write("")
st.sidebar.title("Painel do Coronavirus (COVID-19) de Mamanguape-PB")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("Projeto independente com objetivo único de informar a população sobre a situação epidemiológica do Município de Mamanguape da Paraíba.")
for i in range(20):
    st.sidebar.write("")
st.sidebar.write("Autor: Luiz Fernando Costa dos Santos, Graduando em Ciência de Dados e Inteligência Artificial (UFPB)")
st.sidebar.write("Fonte: Prefeitura Municipal de Mamanguape")


st.header("Casos Confirmados Acumulados")
st.plotly_chart(fig)

st.header("Óbitos Confirmados Acumulados")
st.plotly_chart(fig3)

st.header("Casos Confirmados por Notificação")
st.plotly_chart(fig2)

st.header("Óbitos Confirmados por Notificação")
st.plotly_chart(fig4)

st.title("Estatísticas")

st.header("Casos Confirmados")
st.subheader("Média:")
st.latex(f"{med_casos:.2f}")
st.subheader("Valor Máximo:")
st.latex(max_casos)

st.header("Óbitos Confirmados")
st.subheader("Média:")
st.latex(f"{med_obt:.2f}")
st.subheader("Valor Máximo:")
st.latex(max_obt)

for i in range(5):
    st.write("")

st.header("Histograma dos Casos Confirmados")
st.plotly_chart(fig6)

st.header("Histograma dos Óbitos Confirmados")
st.plotly_chart(fig5)
