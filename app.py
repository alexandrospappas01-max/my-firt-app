import streamlit as st
import datetime
import time

# Ρύθμιση σελίδας
st.set_page_config(page_title="School Schedule", layout="centered")

# --- STYLE ΓΙΑ ΤΑ ΠΑΝΤΑ ΔΙΠΛΑ-ΔΙΠΛΑ ---
st.markdown(
    """
    <style>
    /* Αυτό το κομμάτι αναγκάζει τις στήλες να μην πέφτουν η μία κάτω από την άλλη */
    [data-testid="column"] {
        width: 50% !important;
        flex: 1 1 50% !important;
        min-width: 50% !important;
    }
    /* Μικραίνουμε λίγο τα γράμματα για να χωράνε άνετα */
    .small-font {
        font-size: 13px !important;
    }
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
    </style>
    <div class="footer">Προγραμματιστής: Κωνσταντίνος Παππάς</div>
    """,
    unsafe_allow_html=True
)

def get_mathimata(mera_idx):
    schedule = {
        0: ["Λογοτεχνία", "Μαθηματικά", "Ιστορία", "Γεωγραφία", "Οδύσσεια", "Γεωγραφία"],
        1: ["Γαλλικά", "Αρχαία", "Ν.Γλώσσα", "Ν.Γλώσσα", "Οδύσσεια", "Γαλλικά", "Αγγλικά"],
        2: ["Μαθηματικά", "Πληροφορική", "Βιολογία", "Γεωμετρία", "Εργαστήρια", "Οικ. Οικ.", "Θρησκευτικά"],
        3: ["Αρχαία", "Λογοτεχνία", "Γυμναστική", "Ιστορία", "Ν.Γλώσσα", "Θρησκευτικά"],
        4: ["Τεχνολογία", "Πληροφορική", "Αγγλικά", "Φυσική", "Γυμναστική"]
    }
    return schedule.get(mera_idx, [])

# --- ΠΑΝΩ ΜΕΡΟΣ ---
st.caption("🕒 Έξυπνο Ρολόι & Πρόγραμμα")

imeres_gr = ["Δευτέρα", "Τρίτη", "Τετάρτη", "Πέμπτη", "Παρασκευή", "Σάββατο", "Κυριακή"]
tora = datetime.datetime.now()
tora_gr = tora + datetime.timedelta(hours=2)

mera_tora = tora_gr.weekday()
mera_avrio = (mera_tora + 1) % 7

# Μπλε πλαίσιο με ώρα
st.info(f"📅 {imeres_gr[mera_tora]} {tora_gr.day}/{tora_gr.month} | ⏰ {tora_gr.hour:02d}:{tora_gr.minute:02d}:{tora_gr.second:02d}")

st.divider()

# --- ΤΑ ΜΑΘΗΜΑΤΑ ΔΙΠΛΑ-ΔΙΠΛΑ ---
col_left, col_right = st.columns(2)

with col_left:
    st.markdown("**Σήμερα**")
    math_tora = get_mathimata(mera_tora)
    if math_tora:
        for m in math_tora:
            st.markdown(f"<div class='small-font'>🔹 {m}</div>", unsafe_allow_html=True)
    else:
        st.write("🎉")

with col_right:
    st.markdown("**Αύριο**")
    math_avrio = get_mathimata(mera_avrio)
    if math_avrio:
        for m in math_avrio:
            st.markdown(f"<div class='small-font'>🔹 {m}</div>", unsafe_allow_html=True)
    else:
        st.write("🎉")

time.sleep(10)
st.rerun()
