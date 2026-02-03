import streamlit as st
import datetime
import time

# Τίτλος του App
st.title("Το Ψηφιακό μου Ρολόι 🕒")


st.success("Κατασκευή : Αλέξανδρος Παππάς!")

placeholder = st.empty()

# Παίρνουμε την τρέχουσα ημερομηνία και ώρα
while True:
    tora = datetime.datetime.now()

# Δημιουργούμε το κείμενο για την ημερομηνία και την ώρα
imerominia = f"{tora.day}/{tora.month}/{tora.year}"
ora = f"{tora.hour + 2:02d}:{tora.minute:02d}:{tora.second:02d}" # Το :02d κρατάει δύο ψηφία (π.χ. 09 αντί για 9)

with placeholder.container():
        st.metric(label="Ημερομηνία", value=imerominia)
        st.metric(label="Ώρα (Ελλάδος)", value=ora)
   
time.sleep(1)
