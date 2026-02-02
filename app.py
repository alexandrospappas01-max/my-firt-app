import streamlit as st

name = st.text_input("Παρακαλώ γράψε το όνομα σου :")
if name.lower() in ["κώστας","γιάννης","αλέξανδρος"]:
    st.success(f"Καλώς όρισες {name}!")
    st.write("Καλώς όρισες " + name)
else:
    st.write("Δεν είσαι στην λίστα " + name)
    st.declined(f"Δεν είσαι στην λίστα {name}!")
