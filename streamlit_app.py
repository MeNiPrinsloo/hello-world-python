import streamlit as st

st.title("Hello, World! 🐍")

name = st.text_input("What is your name?")
st.caption("🕺🏽🎤👀🎶 I always feel like someone is watching me...")

if name:
    st.write("Hello, " + name + "!")
