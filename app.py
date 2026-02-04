import streamlit as st
import datetime

# Ρύθμιση σελίδας
st.set_page_config(page_title="Πρόγραμμα Κωνσταντίνου", layout="centered")

# --- STYLE ΓΙΑ ΤΟ ΟΝΟΜΑ ΠΡΟΓΡΑΜΜΑΤΙΣΤΗ ---
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 50px;
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
st.title("📚 Πρόγραμμα Μαθημάτων")

imeres_gr = ["Δευτέρα", "Τρίτη", "Τετάρτη", "Πέμπτη", "Παρασκευή", "Σάββατο", "Κυριακή"]

tora = datetime.datetime.now()
# Προσαρμογή ώρας Ελλάδος αν το server είναι σε άλλη ζώνη
tora_gr = tora + datetime.timedelta(hours=2)

mera_tora = tora_gr.weekday()
mera_avrio = (mera_tora + 1) % 7

onoma_tora = imeres_gr[mera_tora]
onoma_avrio = imeres_gr[mera_avrio]

# Εμφάνιση Ημερομηνίας
st.info(f"📅 Σήμερα είναι **{onoma_tora} {tora_gr.day}/{tora_gr.month}/{tora_gr.year}**")

st.divider()

col_left, col_right = st.columns(2)

with col_left:
    st.subheader(f"✅ Σήμερα ({onoma_tora})")
    list_tora = get_mathimata(mera_tora)
    if list_tora:
        for m in list_tora:
            st.write(f"🔹 {m}")
    else:
        st.write("🎉 Ξεκούραση!")

with col_right:
    st.subheader(f"➡️ Αύριο ({onoma_avrio})")
    list_avrio = get_mathimata(mera_avrio)
    if list_avrio:
        for m in list_avrio:
            st.write(f"🔹 {m}")
    else:
        st.write("🎉 Ξεκούραση!")

# Κουμπί για χειροκίνητη ανανέωση αν χρειαστεί
if st.button("Ανανέωση Ώρας"):
    st.rerun()
