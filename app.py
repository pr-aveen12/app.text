import streamlit as st
st.title ("💫⭐MY FIRST STREAMLIT APP")

name=st.text_input("Enter your Name")

if st.button("Submit"):
   st.write(f"Hello,{Name}")
