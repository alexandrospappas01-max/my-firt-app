import streamlit as st
import datetime
import time

# Ρύθμιση σελίδας
st.set_page_config(page_title="School Schedule", layout="centered")

# --- STYLE ΓΙΑ ΑΝΑΔΕΙΞΗ ΓΡΑΜΜΑΤΩΝ & ΔΙΠΛΟ GRADIENT ---
st.markdown(
    """
    <style>
    .stApp {
        /* Διαβάθμιση: Σκούρο μπλε πάνω/κάτω, πολύ ανοιχτό στο κέντρο */
        background: linear-gradient(180deg, #1e3a8a 0%, #f0f9ff 35%, #f0f9ff 65%, #1e3a8a 100%);
        background-attachment: fixed;
    }
    
    .block-container {
        padding-top: 3rem; 
        padding-bottom: 5rem;
    }
    
    /* Ανάδειξη τίτλων με σκιά για να "βγαίνουν" μπροστά */
    .centered-text {
        text-align: center;
        margin-top: 0px;
        margin-bottom: 0px;
        line-height: 1.2;
        color: #0f172a;
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8);
    }
    
    /* Ο τίτλος στην κορυφή που είναι πάνω στο σκούρο χρώμα */
    .top-title {
        color: #ffffff !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5) !important;
    }

    /* Πίνακας με έντονο λευκό φόντο και σκιές στις γωνίες */
    .stTable {
        background-color: white !important;
        border-radius: 15px !important;
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.1);
        padding: 15px;
        margin-top: 15px;
    }

    .stSelectbox {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
    }

    hr {
        border-top: 2px solid #1e3a8a !important;
        opacity: 0.2;
    }

    /* Programmed by: Λευκά γράμματα γιατί είναι πάνω στο σκούρο μπλε κάτω μέρος */
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
        # Εδώ χρησιμοποιούμε την κλάση 'top-title' για τα πάνω γράμματα
        st.markdown("<h3 class='centered-text top-title'>🕒 Έξυπνο Ρολόι</h3>", unsafe_allow_html=True)
        st.markdown(f"<h5 class='centered-text top-title'>📅 {imeres_gr[tora_gr.weekday()]} {tora_gr.day}/{tora_gr.month}</h5>", unsafe_allow_html=True)
        st.markdown(f"<h5 class='centered-text top-title'>⏰ {tora_gr.hour:02d}:{tora_gr.minute:02d}:{tora_gr.second:02d}</h5>", unsafe_allow_html=True)
        
        st.markdown(f"<h4 class='centered-text' style='margin-top:15px;'>📚 Πρόγραμμα: {titlos_1}</h4>", unsafe_allow_html=True)
        
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
