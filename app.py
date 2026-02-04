import streamlit as st
import datetime
import time

# Ρύθμιση σελίδας
st.set_page_config(page_title="School Schedule", layout="centered")

# --- STYLE ΓΙΑ ΑΝΑΔΕΙΞΗ ΜΑΥΡΩΝ ΓΡΑΜΜΑΤΩΝ ---
st.markdown(
    """
    <style>
    .stApp {
        /* Διαβάθμιση: Πιο ανοιχτό πάνω για να φαίνονται τα μαύρα γράμματα */
        background: linear-gradient(180deg, #bae6fd 0%, #f0f9ff 30%, #f0f9ff 70%, #1e3a8a 100%);
        background-attachment: fixed;
    }
    
    .block-container {
        padding-top: 3rem; 
        padding-bottom: 5rem;
    }
    
    /* Μαύρα γράμματα για το Ρολόι, Ημερομηνία, Ώρα */
    .black-text {
        text-align: center;
        margin-top: 0px;
        margin-bottom: 0px;
        line-height: 1.1;
        color: #000000 !important;
        font-weight: bold;
        text-shadow: 1px 1px 1px rgba(255, 255, 255, 0.5);
    }
    
    .centered-text {
        text-align: center;
        margin-top: 0px;
        margin-bottom: 0px;
        line-height: 1.2;
        color: #0f172a;
        font-weight: bold;
    }

    /* Ανέβασμα πίνακα 1 γραμμή πάνω */
    .stTable {
        background-color: white !important;
        border-radius: 15px !important;
        box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.1);
        padding: 10px;
        margin-top: -5px; /* Ανέβηκε */
    }

    hr {
        margin-top: 10px !important;
        margin-bottom: 10px !important;
        border-top: 2px solid #1e3a8a !important;
        opacity: 0.2;
    }

    .footer {
        position: fixed;
        left: 0;
        bottom: 50px; 
        width: 100%;
        text-align: right;
        padding-right: 20px;
        font-size: 14px;
        font-weight: bold;
        color: #ffffff;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
        z-index: 999;
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

imeres_gr = ["Δευτέρα", "Τρίτη", "Τετάρτη", "Πέμπτη", "Παρασκευή", "Σάββατο", "Κυριακή"]

option = st.selectbox(
    "📅 Επιλογή ημέρας:",
    ["Αυτόματα (Σήμερα & Αύριο)"] + imeres_gr
)

placeholder = st.empty()

while True:
    tora = datetime.datetime.now()
    tora_gr = tora + datetime.timedelta(hours=2)
    
    if option == "Αυτόματα (Σήμερα & Αύριο)":
        mera_deikshs_1 = tora_gr.weekday()
        titlos_1 = "Σήμερα"
        mera_deikshs_2 = (mera_deikshs_1 + 1) % 7
        onoma_avrio = imeres_gr[mera_deikshs_2]
        titlos_2 = f"Αύριο ({onoma_avrio})"
    else:
        mera_deikshs_1 = imeres_gr.index(option)
        titlos_1 = option
        mera_deikshs_2 = (mera_deikshs_1 + 1) % 7
        onoma_epomeni = imeres_gr[mera_deikshs_2]
        titlos_2 = f"Επόμενη ({onoma_epomeni})"

    with placeholder.container():
        # Εφαρμογή της κλάσης 'black-text'
        st.markdown("<h3 class='black-text'>🕒 Έξυπνο Ρολόι</h3>", unsafe_allow_html=True)
        st.markdown(f"<h5 class='black-text'>📅 {imeres_gr[tora_gr.weekday()]} {tora_gr.day}/{tora_gr.month}</h5>", unsafe_allow_html=True)
        st.markdown(f"<h5 class='black-text'>⏰ {tora_gr.hour:02d}:{tora_gr.minute:02d}:{tora_gr.second:02d}</h5>", unsafe_allow_html=True)
        
        st.markdown(f"<h4 class='centered-text' style='margin-top:10px;'>📚 Πρόγραμμα: {titlos_1}</h4>", unsafe_allow_html=True)
        
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
