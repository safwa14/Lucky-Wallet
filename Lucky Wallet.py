import streamlit as st
import random

st.title("💸 Whose Wallet?")
st.write("Welcome to 'whose wallet!' 👋")
st.write("You will give me a list of names, and I will pick a person to pay.")

names_string = st.text_input("If you're ready, enter the names separated by a comma:")

if st.button("Pick someone to pay"):
    if names_string.strip():
        names = [name.strip() for name in names_string.split(",") if name.strip()]
        if names:
            chosen = random.choice(names)
            st.success(f"Please ask *{chosen}* to take their wallet out. Dinner is on them 😅")
        else:
            st.warning("Please enter at least one valid name.")
    else:
        st.warning("You must enter some names first.")
