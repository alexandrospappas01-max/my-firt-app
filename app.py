import streamlit as st
import datetime
import time

# Ρύθμιση σελίδας
st.set_page_config(page_title="School Schedule", layout="centered")

# --- STYLE ΓΙΑ ΣΥΜΠΑΓΗ ΕΜΦΑΝΙΣΗ & DEVELOPER CREDIT ---
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 5rem;
    }
    .centered-text {
        text-align: center;
        margin-top: 2px;
        margin-bottom: 2px;
        line-height: 1.2;
    }
    .stTable {
        margin-top: -10px;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 80px; 
        width: 100%;
        text-align: right;
        padding-right: 20px;
        font-size: 13px;
        font-weight: bold;
        color: #4F4F4F;
        z-index: 999;
    }
    /* Στυλ για το selectbox να φαίνεται όμορφα */
    .stSelectbox {
        margin-bottom: 20px;
    }
    </style>
    <div class="footer">Programmed by: Κωνσταντίνος Παππάς</div>
    """, 
    unsafe_allow_html=True
)

def get_mathimata(mera_idx):
    schedule = {
        0: ["Λογοτεχνία", "Μαθηματικά", "Ιστορία", "Γεωγραφία", "Οδύσσεια", "Γεωγραφία", "-"],
        1: ["Γαλλικά", "Αρχαία", "Ν.Γλώσσα", "Ν.Γλώσσα", "Οδύσσεια", "Γαλλικά", "Αγγλικά"],
        2: ["Μαθηματικά", "Πληροφορική", "Βιολογία", "Γεωμετρία", "Εργαστήρια", "Οικ. Οικ.", "Θρησκευτικά"],
        3: ["Αρχαία", "Λογοτεχνία", "Γυμναστική", "Ιστορία", "Ν.Γλώσσα", "Θρησκευτικά", "-"],
        4: ["Τεχνολογία", "Πληροφορική", "Αγγλικά", "Φυσική", "Γυμναστική", "-", "-"],
        5: ["-", "-", "Σάββατο", "-", "-", "-", "-"],
        6: ["-", "-", "Κυριακή", "-", "-", "-", "-"]
    }
    return schedule.get(mera_idx, ["-", "-", "-", "-", "-", "-", "-"])

# Προσθήκη επιλογής ημέρας στο sidebar ή στην κορυφή
imeres_gr = ["Δευτέρα", "Τρίτη", "Τετάρτη", "Πέμπτη", "Παρασκευή", "Σάββατο", "Κυριακή"]
option = st.selectbox(
    "📅 Επιλογή προβολής προγράμματος:",
    ["Αυτόματα (Σήμερα & Αύριο)"] + imeres_gr
)

placeholder = st.empty()

while True:
    tora = datetime.datetime.now()
    tora_gr = tora + datetime.timedelta(hours=2)
    
    # Λογική επιλογής ημέρας
    if option == "Αυτόματα (Σήμερα & Αύριο)":
        mera_deikshs_1 = tora_gr.weekday()
        titlos_1 = "Σήμερα"
        mera_deikshs_2 = (mera_deikshs_1 + 1) % 7
        titlos_2 = "Αύριο"
    else:
        # Αν ο χρήστης διάλεξε συγκεκριμένη μέρα
        mera_deikshs_1 = imeres_gr.index(option)
        titlos_1 = option
        mera_deikshs_2 = (mera_deikshs_1 + 1) % 7
        titlos_2 = "Επόμενη ημέρα"

    with placeholder.container():
        st.markdown("<h2 class='centered-text'>🕒 Έξυπνο Ρολόι</h2>", unsafe_allow_html=True)
        st.markdown(f"<h4 class='centered-text'>📅 {imeres_gr[tora_gr.weekday()]} {tora_gr.day}/{tora_gr.month}/{tora_gr.year}</h4>", unsafe_allow_html=True)
        st.markdown(f"<h4 class='centered-text'>⏰ {tora_gr.hour:02d}:{tora_gr.minute:02d}:{tora_gr.second:02d}</h4>", unsafe_allow_html=True)
        
        st.markdown(f"<h3 class='centered-text'>📚 Πρόγραμμα: {titlos_1}</h3>", unsafe_allow_html=True)
        
        st.divider()

        math_1 = get_mathimata(mera_deikshs_1)
        math_2 = get_mathimata(mera_deikshs_2)
        
        data = []
        for i in range(len(math_1)):
            data.append({
                "Ώρα": f"{i+1}η",
                titlos_1: math_1[i],
                titlos_2: math_2[i]
            })
        
        st.table(data)

    time.sleep(1)
