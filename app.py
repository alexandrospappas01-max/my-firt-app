
import streamlit as st
import datetime
import time  # ΠΡΟΣΟΧΗ: Χρειάζεται οπωσδήποτε αυτό!

st.title("Το Ψηφιακό μου Ρολόι 🕒")
st.success("Κατασκευή: Αλέξανδρος Παππάς!")

# Δημιουργούμε έναν κενό χώρο για να ανανεώνεται το ρολόι
placeholder = st.empty()

while True:
    tora = datetime.datetime.now()
    
    # Διαμόρφωση ώρας και ημερομηνίας
    imerominia = f"{tora.day}/{tora.month}/{tora.year}"
    ora = f"{tora.hour + 2:02d}:{tora.minute:02d}:{tora.second:02d}"

    # Σχεδιάζουμε το ρολόι ΜΕΣΑ στον κενό χώρο
    with placeholder.container():
        st.metric(label="Ημερομηνία", value=imerominia)
        st.metric(label="Ώρα (Ελλάδος)", value=ora)
st.write("Τωρα τρέχουν και τα δευτερόλεπτα")
    # Περίμενε 1 δευτερόλεπτο
    time.sleep(1)
