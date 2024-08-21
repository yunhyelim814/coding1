import streamlit as st

st.header("Hello")

isClicked= st.button("이거 누르면 바보")
if isClicked :
  st.write("너 참 귀엽다")
