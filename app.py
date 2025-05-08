import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Analisis salarial base wooldridge")

tab1, tab2 = st.tabs(["analisis univariado","analisis bivariado"])

wage=pd.read_csv("wage.csv")


with tab1:
    fig, ax = plt.subplots(1,1)
    ax.hist(wage["salario"].dropna())
    ax.set_title("Salario")
    ax.axis()
    st.pyplot(fig)

    fig, ax = plt.subplots(1,1)
    ax.hist(wage["educacion"].dropna())
    ax.set_title("Educación")
    ax.axis()
    st.pyplot(fig)

    fig, ax = plt.subplots(1,1)
    ax.hist(wage["experiencia"].dropna())
    ax.set_title("Experiencia")
    ax.axis()
    st.pyplot(fig)

    fig, ax = plt.subplots(1,1)
    ax.hist(wage["genero"].dropna())
    ax.set_title("Genero")
    ax.axis()
    st.pyplot(fig)


with tab2:
    fig, ax = plt.subplots(1,1)
    sns.boxplot(y = wage["salario"], x=wage["genero"].dropna())
    ax.set_title("Salario vs genero")
    ax.axis()
    st.pyplot(fig)

    fig, ax = plt.subplots(1,1)
    ax.scatter(y = wage["salario"], x=wage["educacion"].dropna())
    ax.set_title("Salario vs educación")
    ax.axis()
    st.pyplot(fig)

    fig, ax = plt.subplots(1,1)
    ax.scatter(y = wage["salario"], x=wage["experiencia"].dropna())
    ax.set_title("Salario vs experiencia")
    ax.axis()
    st.pyplot(fig)




#scatter boxplot

