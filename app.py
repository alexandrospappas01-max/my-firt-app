import streamlit as st

name = st.text_input("Παρακαλώ γράψε το όνομα σου :")
name = name.lower()
if (name == "Κώστας") or (name == "Γιάννης") or (name == "αλέξανδρος"):
    st.write("Καλώς όρισες " + name)
else:
    st.write("Δεν είσαι στην λίστα " + name)
