import streamlit as st
import datetime
import time

# Ρύθμιση για συμπαγή εμφάνιση και τίτλο
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
    if mera_idx == 0: # Δευτέρα
        return ["Λογοτεχνία", "Μαθηματικά", "Ιστορία", "Γεωγραφία", "Οδύσσεια", "Γεωγραφία"]
    elif mera_idx == 1: # Τρίτη
        return ["Γαλλικά", "Αρχαία", "Ν.Γλώσσα", "Ν.Γλώσσα", "Οδύσσεια", "Γαλλικά", "Αγγλικά"]
    elif mera_idx == 2: # Τετάρτη
        return ["Μαθηματικά", "Πληροφορική", "Βιολογία", "Γεωμετρία", "Εργαστήρια", "Οικ. Οικ.", "Θρησκευτικά"]
    elif mera_idx == 3: # Πέμπτη
        return ["Αρχαία", "Λογοτεχνία", "Γυμναστική", "Ιστορία", "Ν.Γλώσσα", "Θρησκευτικά"]
    elif mera_idx == 4: # Παρασκευή
        return ["Τεχνολογία", "Πληροφορική", "Αγγλικά", "Φυσική", "Γυμναστική"]
    else:
        return []

# --- ΚΥΡΙΩΣ ΠΡΟΓΡΑΜΜΑ ---
st.caption("🕒 Έξυπνο Ρολόι & Πρόγραμμα")

imeres_gr = ["Δευτέρα", "Τρίτη", "Τετάρτη", "Πέμπτη", "Παρασκευή", "Σάββατο", "Κυριακή"]

# Ρολόι σε μια γραμμή
col_time = st.empty()

# Χώρος για τα δύο προγράμματα
schedule_area = st.empty()

while True:
    tora = datetime.datetime.now()
    mera_tora = tora.weekday()
    # Υπολογισμός επόμενης μέρας (αν είναι Κυριακή (6), η επόμενη είναι Δευτέρα (0))
    mera_avrio = (mera_tora + 1) % 7
    
    onoma_tora = imeres_gr[mera_tora]
    onoma_avrio = imeres_gr[mera_avrio]

    # Ενημέρωση Ρολογιού
    imerominia = f"{onoma_tora} {tora.day}/{tora.month}"
    ora = f"{tora.hour + 2:02d}:{tora.minute:02d}:{tora.second:02d}"
    col_time.write(f"📅 {imerominia} | ⏰ {ora}")
    
    with schedule_area.container():
        left, right = st.columns(2)
        
        with left:
            st.write(f"**Σήμερα: {onoma_tora}**")
            list_tora = get_mathimata(mera_tora)
            if list_tora:
                for m in list_tora:
                    st.write(f"▫️{m}", style="font-size: 12px;")
            else:
                st.write("🎉 Ξεκούραση")

        with right:
            st.write(f"**Αύριο: {onoma_avrio}**")
            list_avrio = get_mathimata(mera_avrio)
            if list_avrio:
                for m in list_avrio:
                    st.write(f"▫️{m}")
            else:
                st.write("🎉 Ξεκούραση")

    time.sleep(1)
