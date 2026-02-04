import streamlit as st
import datetime

# Ρύθμιση για να είναι καθαρή η οθόνη
st.set_page_config(page_title="School Schedule", layout="centered")

# --- STYLE ΓΙΑ ΤΟ ΟΝΟΜΑ & ΣΤΗΛΕΣ ---
st.markdown(
    """
    <style>
    /* Καθαρίζει τα περιττά κενά */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
    }
    /* Αναγκάζει τις στήλες να μένουν δίπλα-δίπλα στο κινητό */
    [data-testid="column"] {
        width: 50% !important;
        flex: 1 1 50% !important;
        min-width: 50% !important;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 20px;
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

# --- ΕΜΦΑΝΙΣΗ ΠΡΟΓΡΑΜΜΑΤΟΣ ---
st.caption("🕒 Έξυπνο Ρολόι & Πρόγραμμα")

imeres_gr = ["Δευτέρα", "Τρίτη", "Τετάρτη", "Πέμπτη", "Παρασκευή", "Σάββατο", "Κυριακή"]
tora = datetime.datetime.now()
# Ώρα Ελλάδος
tora_gr = tora + datetime.timedelta(hours=2)
mera_tora = tora_gr.weekday()
mera_avrio = (mera_tora + 1) % 7

# Μπλε πλαίσιο με την ώρα (σταθερό, χωρίς δευτερόλεπτα που τρέχουν για να μην κολλάει)
st.info(f"📅 {imeres_gr[mera_tora]} {tora_gr.day}/{tora_gr.month} | ⏰ {tora_gr.hour:02d}:{tora_gr.minute:02d}")

st.divider()

col_left, col_right = st.columns(2)

with col_left:
    st.write("**Σήμερα**")
    math_tora = get_mathimata(mera_tora)
    if math_tora:
        for m in math_tora:
            st.write(f"🔹 {m}")
    else:
        st.write("🎉 Ξεκούραση")

with col_right:
    st.write("**Αύριο**")
    math_avrio = get_mathimata(mera_avrio)
    if math_avrio:
        for m in math_avrio:
            st.write(f"🔹 {m}")
    else:
        st.write("🎉 Ξεκούραση")
