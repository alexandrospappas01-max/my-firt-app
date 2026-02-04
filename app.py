import streamlit as st
import datetime
import time

# Ρύθμιση για συμπαγή εμφάνιση
st.set_page_config(page_title="School Clock", layout="centered")

# --- STYLE ΓΙΑ ΤΟ ΟΝΟΜΑ ΚΑΤΩ ΔΕΞΙΑ ---
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 10px;
        width: 100%;
        text-align: right;
        padding-right: 20px;
        font-size: 12px;
        color: gray;
    }
    </style>
    <div class="footer">Προγραμματιστής: Κωνσταντίνος Παππάς</div>
    """,
    unsafe_allow_html=True
)

# --- ΚΥΡΙΩΣ ΠΡΟΓΡΑΜΜΑ ---
st.subheader("🕒 Το Έξυπνο Ρολόι μου")

imeres_gr = ["Δευτέρα", "Τρίτη", "Τετάρτη", "Πέμπτη", "Παρασκευή", "Σάββατο", "Κυριακή"]

col1, col2 = st.columns(2)
with col1:
    date_placeholder = st.empty()
with col2:
    time_placeholder = st.empty()

school_placeholder = st.empty()

while True:
    tora = datetime.datetime.now()
    mera_num = tora.weekday()
    onoma_meras = imeres_gr[mera_num]

    # Ημερομηνία και Ώρα (+2 για Ελλάδα)
    imerominia_full = f"{onoma_meras} {tora.day}/{tora.month}/{tora.year}"
    ora_full = f"{tora.hour + 2:02d}:{tora.minute:02d}:{tora.second:02d}"

    date_placeholder.caption(f"📅 **{imerominia_full}**")
    time_placeholder.caption(f"⏰ **{ora_full}**")
    
    with school_placeholder.container():
        st.write(f"**Πρόγραμμα Σήμερα: {onoma_meras}**")
        
        if mera_num == 0: # Δευτέρα
            mathimata = ["1η Λογοτεχνία", "2η Μαθηματικά", "3η Ιστορία", "4η Γεωγραφία", "5η Οδύσσεια", "6η Γεωγραφία"]
        elif mera_num == 1: # Τρίτη
            mathimata = ["1η Γαλλικά", "2η Αρχαία", "3η Ν.Γλώσσα", "4η Ν.Γλώσσα", "5η Οδύσσεια", "6η Γαλλικά", "7η Αγγλικά"]
        elif mera_num == 2: # Τετάρτη
            mathimata = ["1η Μαθηματικά", "2η Πληροφορική", "3η Βιολογία", "4η Γεωμετρία", "5η Εργαστήρια", "6η Οικ. Οικονομία", "7η Θρησκευτικά"]
        elif mera_num == 3: # Πέμπτη
            mathimata = ["1η Αρχαία", "2η Λογοτεχνία", "3η Γυμναστική", "4η Ιστορία", "5η Ν.Γλώσσα", "6η Θρησκευτικά"]
        elif mera_num == 4: # Παρασκευή
            mathimata = ["1η Τεχνολογία", "2η Πληροφορική", "3η Αγγλικά", "4η Φυσική", "5η Γυμναστική"]
        else:
            mathimata = []

        if mathimata:
            for m in mathimata:
                st.write(f"🔹 {m}")
        else:
            st.write("🎉 Σαββατοκύριακο! Ξεκούραση!")

    time.sleep(1)
