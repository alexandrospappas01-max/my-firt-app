
import streamlit as st
import datetime
import time

st.title("Το Έξυπνο Ρολόι & Πρόγραμμα 🕒📚")
st.success("Programized by: Κωνσταντίνος Παππάς!")

# Δημιουργούμε έναν χώρο για το ρολόι και έναν για το πρόγραμμα
clock_placeholder = st.empty()
school_placeholder = st.empty()

while True:
    tora = datetime.datetime.now()
    
    # 1. Εμφάνιση Ρολογιού
    imerominia = f"{tora.day}/{tora.month}/{tora.year}"
    ora = f"{tora.hour + 2:02d}:{tora.minute:02d}:{tora.second:02d}"

    with clock_placeholder.container():
        st.metric(label="Ημερομηνία", value=imerominia)
        st.metric(label="Ώρα Ελλάδος", value=ora)
    
    # 2. Αυτόματη εμφάνιση προγράμματος ανάλογα με τη μέρα
    # weekday(): 0=Δευτέρα, 1=Τρίτη, 2=Τετάρτη, 3=Πέμπτη, 4=Παρασκευή
    mera_num = tora.weekday() 

    with school_placeholder.container():
        st.subheader("📖 Το Πρόγραμμα των Μαθημάτων σου:")
        
        if mera_num == 0: # Δευτέρα
            st.write("1η Λογοτεχνία | 2η Μαθηματικά | 3η Ιστορία | 4η Γεωγραφία | 5η Οδύσσεια | 6η Γεωγραφία")
        
        elif mera_num == 1: # Τρίτη
            st.write("1η Γαλλικά | 2η Αρχαία | 3η Ν.Γλώσσα | 4η Ν.Γλώσσα | 5η Οδύσσεια | 6η Γαλλικά | 7η Αγγλικά")
            
        elif mera_num == 2: # Τετάρτη
            st.write("1η Μαθηματικά | 2η Πληροφορική | 3η Βιολογία | 4η Γεωμετρία | 5η Εργαστήρια | 6η Οικιακή Οικονομία | 7η Θρησκευτικά")
            
        elif mera_num == 3: # Πέμπτη
            st.write("1η Αρχαία | 2η Λογοτεχνία | 3η Γυμναστική | 4η Ιστορία | 5η Ν.Γλώσσα | 6η Θρησκευτικά")
            
        elif mera_num == 4: # Παρασκευή
            st.write("1η Τεχνολογία | 2η Πληροφορική | 3η Αγγλικά | 4η Φυσική | 5η Γυμναστική")
            
        else: # Σαββατοκύριακο
            st.balloons()
            st.write("🎉 Είναι Σαββατοκύριακο! Ξεκούραση και παιχνίδι!")

    # Ανανέωση κάθε δευτερόλεπτο
    time.sleep(1)
