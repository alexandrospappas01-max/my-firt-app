import streamlit as st
import datetime
import time

# Ρύθμιση για συμπαγή εμφάνιση
st.set_page_config(page_title="School Schedule", layout="centered")

# --- STYLE ΓΙΑ ΤΟ ΟΝΟΜΑ ΠΡΟΓΡΑΜΜΑΤΙΣΤΗ ---
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 100px;
        width: 100%;
        text-align: right;
        padding-right: 20px;
        font-size: 13px;
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
    # Επιστρέφει τη λίστα μαθημάτων ανάλογα με τον αριθμό της ημέρας
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
mera_tora = tora.weekday()
mera_avrio = (mera_tora + 1) % 7

onoma_tora = imeres_gr[mera_tora]
onoma_avrio = imeres_gr[mera_avrio]

# Εμφάνιση Ρολογιού (Ώρα Ελλάδος)
imerominia = f"{onoma_tora} {tora.day}/{tora.month}"
ora = f"{tora.hour + 2:02d}:{tora.minute:02d}:{tora.second:02d}"
st.write(f"📅 {imerominia} | ⏰ {ora}")

st.divider() # Μια μικρή διαχωριστική γραμμή

left, right = st.columns(2)

with left:
    st.write(f"**Σήμερα: {onoma_tora}**")
    list_tora = get_mathimata(mera_tora)
    if list_tora:
        for m in list_tora:
            st.write(f"▫️ {m}")
    else:
        st.write("🎉 Ξεκούραση")

with right:
    st.write(f"**Αύριο: {onoma_avrio}**")
    list_avrio = get_mathimata(mera_avrio)
    if list_avrio:
        for m in list_avrio:
            st.write(f"▫️ {m}")
    else:
        st.write("🎉 Ξεκούραση")

# Αντί για while True, περιμένουμε 1 δευτερόλεπτο και ξανατρέχουμε όλο το script
time.sleep(1)
st.rerun()
