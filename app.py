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
        padding-bottom: 5rem; /* Δίνουμε χώρο στο τέλος για να μην κρύβεται ο πίνακας */
    }
    .centered-text {
        text-align: center;
        margin-top: 2px;
        margin-bottom: 2px;
        line-height: 1.2;
    }
    .stTable {
        margin-top: -15px;
    }
    /* Ρύθμιση για το Programmed by - Ανέβηκε κι άλλο */
    .footer {
        position: fixed;
        left: 0;
        bottom: 80px; /* Ανέβηκε σημαντικά για να φαίνεται σε όλα τα κινητά */
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
        4: ["Τεχνολογία", "Πληροφορική", "Αγγλικά", "Φυσική", "Γυμναστική", "-", "-"]
    }
    return schedule.get(mera_idx, ["-", "-", "-", "-", "-", "-", "-"])

placeholder = st.empty()

while True:
    tora = datetime.datetime.now()
    tora_gr = tora + datetime.timedelta(hours=2)
    mera_tora = tora_gr.weekday()
    mera_avrio = (mera_tora + 1) % 7
    imeres_gr = ["Δευτέρα", "Τρίτη", "Τετάρτη", "Πέμπτη", "Παρασκευή", "Σάββατο", "Κυριακή"]

    with placeholder.container():
        # Ρολόι και Ημερομηνία
        st.markdown("<h2 class='centered-text'>🕒 Έξυπνο Ρολόι</h2>", unsafe_allow_html=True)
        st.markdown(f"<h4 class='centered-text'>📅 {imeres_gr[mera_tora]} {tora_gr.day}/{tora_gr.month}/{tora_gr.year}</h4>", unsafe_allow_html=True)
        st.markdown(f"<h4 class='centered-text'>⏰ {tora_gr.hour:02d}:{tora_gr.minute:02d}:{tora_gr.second:02d}</h4>", unsafe_allow_html=True)
        
        # Τίτλος Προγράμματος
        st.markdown("<h3 class='centered-text'>📚 Πρόγραμμα Μαθημάτων</h3>", unsafe_allow_html=True)
        
        st.divider()

        # Πίνακας Μαθημάτων
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
