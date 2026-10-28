
import streamlit as st
import requests

st.title("Hello, World! 🐍")

with st.form("hello_form"):
    name = st.text_input("What is your name?", max_chars=60)

    st.caption("🕺🏽🎤👀🎶 I always feel like someone is watching me...")
    st.caption("Submitted names and timestamps are saved privately. Nicknames welcome!")

    submitted = st.form_submit_button("Say Hello! 💚")

if submitted:
    name = name.strip()

    if name:
        st.write("Hello, " + name + "!")

        try:
            response = requests.post(
                st.secrets["GOOGLE_SCRIPT_URL"],
                json={
                    "name": name,
                    "secret": st.secrets["APP_SECRET"]
                },
                timeout=10
            )

            response.raise_for_status()

            if response.json().get("status") != "Success":
                st.warning("Greeting worked, but the name wasn't saved.")

        except Exception:
            st.warning("Greeting worked, but the name wasn't saved.")

    else:
        st.warning("Please enter a name!")
