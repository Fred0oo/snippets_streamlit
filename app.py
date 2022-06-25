import streamlit as st

# Afficher n'importe quoi texte, df, plot...
# si plusieurs éléments ils s'affichent à la suite verticalement
st.write("hello world!", "df", "plot")

st.title("Title", anchor="title")
st.write("...")

st.header("header", anchor="header")
st.write("...")

st.subheader("subheader", anchor="subheader")
st.write("...")