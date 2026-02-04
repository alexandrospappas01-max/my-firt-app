import streamlit as st
import datetime
import time

# Ρύθμιση σελίδας
st.set_page_config(page_title="School Schedule", layout="centered")

# --- STYLE ΓΙΑ ΤΟ ΟΝΟΜΑ & ΣΤΗΛΕΣ ΣΤΟ ΚΙΝΗΤΟ ---
st.markdown(
    """
    <style>
    /* Φτιάχνει το όνομα κάτω δεξιά */
    .footer {
        position: fixed;
        left: 0;
        bottom: 80px;
        width: 100%;
        text-align: right;
        padding-right: 20px;
        font-size: 12px;
        font-weight: bold;
        color: #4F4F4F;
    }
    /* Αναγκάζει τις στήλες να μένουν δίπλα-δίπλα σε μικρές οθόνες */
    [data-testid="column"] {
        width: 48% !important;
        flex: 1 1 48% !important;
        min-width: 48% !important;
    }
    </style>
    <div class="footer">Προγραμματιστής: Κωνσταντίνος Παππάς</div>
    """,
    unsafe_allow_html=True
)

# --- ΣΥΝΑΡΤΗΣΗ ΓΙΑ ΤΑ ΜΑΘΗΜΑΤΑ ---
def get_mathimata(mera_idx):
    schedule = {
        0: ["Λογοτεχνία", "Μαθηματικά", "Ιστορία", "Γεωγραφία", "Οδύσσεια", "Γεωγραφία"],
        1: ["Γαλλικά", "Αρχαία", "Ν.Γλώσσα", "Ν.Γλώσσα", "Οδύσσεια", "Γαλλικά", "Αγγλικά"],
        2: ["Μαθηματικά", "Πληροφορική", "Βιολογία", "Γεωμετρία", "Εργαστήρια", "Οικ. Οικ.", "Θρησκευτικά"],
        3: ["Αρχαία", "Λογοτεχνία", "Γυμναστική", "Ιστορία", "Ν.Γλώσσα", "Θρησκευτικά"],
        4: ["Τεχνολογία", "Πληροφορική", "Αγγλικά", "Φυσική", "Γυμναστική"]
    }
    return schedule.get(mera_idx, [])

# --- ΚΥΡΙΩΣ ΠΡΟΓΡΑΜΜΑ ---
st.caption("🕒 Έξυπνο Ρολόι & Πρόγραμμα")

imeres_gr = ["Δευτέρα", "Τρίτη", "Τετάρτη", "Πέμπτη", "Παρασκευή", "Σάββατο", "Κυριακή"]

tora = datetime.datetime.now()
tora_gr = tora + datetime.timedelta(hours=2)

mera_tora = tora_gr.weekday()
mera_avrio = (mera_tora + 1) % 7

onoma_tora = imeres_gr[mera_tora]
onoma_avrio = imeres_gr[mera_avrio]

# Ρολόι
imerominia = f"{onoma_tora} {tora_gr.day}/{tora_gr.month}"
ora = f"{tora_gr.hour:02d}:{tora_gr.minute:02d}:{tora_gr.second:02d}"
st.info(f"📅 {imerominia} | ⏰ {ora}")

st.divider()

# Δημιουργία στηλών με μικρό κενό (gap)
col_left, col_right = st.columns(2, gap="small")

with col_left:
    st.write(f"**Σήμερα**")
    list_tora = get_mathimata(mera_tora)
    if list_tora:
        for m in list_tora:
            st.markdown(f"<div style='font-size: 13px;'>🔹 {m}</div>", unsafe_allow_html=True)
    else:
        st.write("🎉")

with col_right:
    st.write(f"**Αύριο**")
    list_avrio = get_mathimata(mera_avrio)
    if list_avrio:
        for m in list_avrio:
            st.markdown(f"<div style='font-size: 13px;'>🔹 {m}</div>", unsafe_allow_html=True)
    else:
        st.write("🎉")

# Ανανέωση
time.sleep(10)
st.rerun()
