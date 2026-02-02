import streamlit as st
import time
with st.status("Γίνεται έλεγχος των δεδομένων..."):
    st.write("Αναζήτηση στη βάση δεδομένων...")
    time.sleep(2) # Χρειάζεται το import time στην αρχή
    st.write("Επιτυχής σύνδεση!")
