import streamlit as st

st.title("Το πρώτο μου web App")
st.write("Καλώς ήρθατε στην εφαρμογή μου.")

name = st.text_input("Πώς σε λένε ;")

if name:
  st.write(f"Γεία σου {name}! Φτιάχνω αυτό το app με την Python!")
  if st.button ("Πάτα για μια έκπληξη"):
    st.butterfly()
 
