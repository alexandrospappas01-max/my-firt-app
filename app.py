import streamlit as st
import datetime
import time
import pandas as pd

# Ρύθμιση σελίδας
st.set_page_config(page_title="School Schedule", layout="centered")

# --- STYLE ΓΙΑ ΜΕΓΑΛΑ ΓΡΑΜΜΑΤΑ & ΟΝΟΜΑ ---
st.markdown(
    """
    <style>
    /* Μεγαλώνει τον τίτλο */
    .big-title {
        font-size: 24px !important;
        font-weight: bold;
        color: #31333F;
        margin-bottom: 10px;
    }
    /* Μεγαλώνει το κείμενο μέσα στον πίνακα */
    .stTable td {
        font-size: 18px !important;
    }
    .stTable th {
        font-size: 20px !important;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 10px;
        width: 100%;
        text-align: right;
        padding-right: 20px;
        font-size: 14px;
        font-weight: bold;
        color: #4F4F4F;
    }
    </style>
    <div class="footer">Προγραμματιστής: Κωνσταντίνος Παππάς</div>
    """, 
    unsafe_allow_html=True
)

def get_mathimata(mera_idx):
    schedule = {
        0: ["Λογοτεχνία", "Μαθηματικά", "Ιστορία", "Γεωγραφία", "Οδύσσεια", "Γεωγραφία", "-"],
        1: ["Γαλλικά", "Αρχαία", "Ν.Γλώσσα", "Ν.Γλώσσα", "Οδύσσεια", "Γαλλικά", "Αγγλικά"],
        2: ["Μαθηματικά", "Πληροφορική", "Βιολογία", "Γεωμετρία", "Εργαστήρια", "Οικ. Οικ.", "Θρησκευτικά"],
        3: ["Αρχαία", "Λογοτεχνία", "Γυμναστική", "Ιστορία", "Ν.Γλώσσα", "Θρησκευτικά", "-"],
        4: ["Τεχνολογία", "Πληροφορική", "Αγγλικά", "Φυσική", "Γυμναστική", "-", "-"]
    }
    return schedule.get(mera_idx, ["-", "-", "-", "-", "-", "-", "-"])

placeholder = st.empty()

while True:
    tora = datetime.datetime.now()
    # Ώρα Ελλάδος
    tora_gr = tora + datetime.timedelta(hours=2)
    mera_tora = tora_gr.weekday()
    mera_avrio = (mera_tora + 1) % 7
    imeres_gr = ["Δευτέρα", "Τρίτη", "Τετάρτη", "Πέμπτη", "Παρασκευή", "Σάββατο", "Κυριακή"]

    with placeholder.container():
        # Μεγάλος Τίτλος
        st.markdown('<div class="big-title">🕒 Έξυπνο Ρολόι & Πρόγραμμα Μαθημάτων</div>', unsafe_allow_html=True)
        
        # Μεγάλο πλαίσιο ώρας
        st.info(f"### 📅 {imeres_gr[mera_tora]} {tora_gr.day}/{tora_gr.month}/{tora_gr.year} |                                                               ⏰ {tora_gr.hour:02d}:{tora_gr.minute:02d}:{tora_gr.second:02d}")
        
        st.write("---")

        # Δημιουργία Πίνακα με αρίθμηση από το 1
        math_tora = get_mathimata(mera_tora)
        math_avrio = get_mathimata(mera_avrio)
        
        # Φτιάχνουμε τα δεδομένα
        df = pd.DataFrame({
            "Σήμερα": math_tora,
            "Αύριο": math_avrio
        })
        
        # Αλλάζουμε το "0, 1, 2" σε "1η, 2η, 3η..."
        df.index = [f"{i+1}η" for i in range(len(df))]
        
        # Εμφάνιση πίνακα
        st.table(df)

    time.sleep(1)
