import streamlit as st
import datetime
import time

# Ρύθμιση σελίδας
st.set_page_config(page_title="School Schedule", layout="centered")

# --- STYLE ---
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
        font-weight: bold;
        color: #4F4F4F;
    }
    /* Στοίχιση κειμένου στο κέντρο για τον τίτλο και το ρολόι */
    .centered-text {
        text-align: center;
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
        # 1. Τίτλος σε δύο γραμμές
        st.markdown("<h3 class='centered-text'>🕒 Έξυπνο Ρολόι &</h3>", unsafe_allow_html=True)
        st.markdown("<h3 class='centered-text'>Πρόγραμμα Μαθημάτων</h3>", unsafe_allow_html=True)
        
        # 2. Ημερομηνία και από κάτω Ώρα
        st.markdown(f"<h4 class='centered-text'>📅 {imeres_gr[mera_tora]} {tora_gr.day}/{tora_gr.month}/{tora_gr.year}</h4>", unsafe_allow_html=True)
        st.markdown(f"<h2 class='centered-text'>⏰ {tora_gr.hour:02d}:{tora_gr.minute:02d}:{tora_gr.second:02d}</h2>", unsafe_allow_html=True)
        
        st.divider()

        # 3. Πίνακας Μαθημάτων
        math_tora = get_mathimata(mera_tora)
        math_avrio = get_mathimata(mera_avrio)
        
        data = []
        for i in range(len(math_tora)):
            data.append({
                "Ώρα": f"{i+1}η",
                "Σήμερα": math_tora[i],
                "Αύριο": math_avrio[i]
            })
        
        st.table(data)

    time.sleep(1)
