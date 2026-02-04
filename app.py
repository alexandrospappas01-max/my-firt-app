import streamlit as st
import datetime
import time

# Ρύθμιση για να πιάνει όλο το πλάτος της οθόνης
st.set_page_config(layout="centered")

# Χρησιμοποιούμε subheader αντί για title για να γλιτώσουμε χώρο
st.subheader("🕒 Το Έξυπνο Ρολόι μου")

# Λίστα με τις ημέρες στα ελληνικά
imeres_gr = ["Δευτέρα", "Τρίτη", "Τετάρτη", "Πέμπτη", "Παρασκευή", "Σάββατο", "Κυριακή"]

# Δημιουργούμε δύο στήλες για Ημερομηνία και Ώρα
col1, col2 = st.columns(2)
with col1:
    date_placeholder = st.empty()
with col2:
    time_placeholder = st.empty()

# Χώρος για το πρόγραμμα
school_placeholder = st.empty()

while True:
    tora = datetime.datetime.now()
    mera_num = tora.weekday()
    onoma_meras = imeres_gr[mera_num]

    # Μορφοποίηση Ημερομηνίας και Ώρας
    imerominia_full = f"{onoma_meras} {tora.day}/{tora.month}/{tora.year}"
    # Χρήση της ώρας Ελλάδος (με βάση τον κώδικα του Αλέξανδρου)
    ora_full = f"{tora.hour + 2:02d}:{tora.minute:02d}:{tora.second:02d}"

    # Ενημέρωση Ημερομηνίας και Ώρας στις στήλες (με μικρότερο κείμενο)
    date_placeholder.caption(f"📅 **{imerominia_full}**")
    time_placeholder.caption(f"⏰ **{ora_full}**")
    
    with school_placeholder.container():
        # Μικρότερος τίτλος για το πρόγραμμα
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
            # Εμφάνιση μαθημάτων σε πολύ συμπαγή μορφή
            for m in mathimata:
                st.write(f"🔹 {m}")
        else:
            st.write("🎉 Σαββατοκύριακο!")

    time.sleep(1)
