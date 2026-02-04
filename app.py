import streamlit as st
import datetime
import time

# Ρύθμιση σελίδας
st.set_page_config(page_title="School Schedule", layout="centered")

# --- STYLE ---
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 3.5rem; 
        padding-bottom: 5rem;
    }
    .centered-text {
        text-align: center;
        margin-top: 0px;
        margin-bottom: 0px;
        line-height: 1.1;
    }
    .stSelectbox {
        margin-top: 10px;
        margin-bottom: 10px;
    }
    .stTable {
        margin-top: 10px;
    }
    hr {
        margin-top: 20px !important;
        margin-bottom: 20px !important;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 60px; 
        width: 100%;
        text-align: right;
        padding-right: 20px;
        font-size: 13px;
        font-weight: bold;
        color: #4F4F4F;
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
        st.markdown("<h3 class='centered-text'>🕒 Έξυπνο Ρολόι</h3>", unsafe_allow_html=True)
        st.markdown(f"<h5 class='centered-text'>📅 {imeres_gr[tora_gr.weekday()]} {tora_gr.day}/{tora_gr.month}</h5>", unsafe_allow_html=True)
        st.markdown(f"<h5 class='centered-text'>⏰ {tora_gr.hour:02d}:{tora_gr.minute:02d}:{tora_gr.second:02d}</h5>", unsafe_allow_html=True)
        
        st.markdown(f"<h4 class='centered-text'>📚 Πρόγραμμα: {titlos_1}</h4>", unsafe_allow_html=True)
        
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
