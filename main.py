import streamlit as st

st.write("""
# My first app
Hello *world!*
I,m a M1k0!!!
@m6rshm3ll0w
""")

number = st.slider("Pick a number", 0, 100)

st.write(f"you pic {number}")