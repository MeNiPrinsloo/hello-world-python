import streamlit as st

st.title("Hello, World! 🐍")

name = st.text_input("What is your name?")

if name:
    st.write("Hello, " + name + "!")