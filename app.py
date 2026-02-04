import streamlit as st
import datetime
import time

# Ρύθμιση σελίδας
st.set_page_config(page_title="School Schedule", layout="centered")

# --- STYLE ΓΙΑ ΤΟ ΟΝΟΜΑ & ΤΟΝ ΠΙΝΑΚΑ ---
st.markdown(
    """
    <style>
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
    /* Στυλ για τον πίνακα μαθημάτων */
    table {
        width: 100%;
        border-collapse: collapse;
    }
    td {
        width: 50%;
        vertical-align: top;
        padding: 5px;
        font-size: 13px;
    }
    .header-text {
        font-weight: bold;
        border-bottom: 2px solid #f0f2f6;
        padding-bottom: 5px;
        margin-bottom: 5px;
    }
    </style>
    <div class="footer">Προγραμματιστής: Κωνσταντίνος Παππάς</div>
    """,
    unsafe_allow_html=True
)

def get_mathimata(mera_idx):
    schedule = {
        0: ["Λογοτεχνία", "Маθηματικά", "Ιστορία", "Γεωγραφία", "Οδύσσεια", "Γεωγραφία"],
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

# --- ΚΑΤΑΣΚΕΥΗ ΠΙΝΑΚΑ ΓΙΑ ΔΙΠΛΑ-ΔΙΠΛΑ ΕΜΦΑΝΙΣΗ ---
math_tora = get_mathimata(mera_tora)
math_avrio = get_mathimata(mera_avrio)

# Βρίσκουμε ποια μέρα έχει τα περισσότερα μαθήματα για να φτιάξουμε τις γραμμές
max_rows = max(len(math_tora), len(math_avrio))

html_table = "<table>"
html_table += "<tr><td><div class='header-text'>Σήμερα</div></td><td><div class='header-text'>Αύριο</div></td></tr>"

for i in range(max_rows):
    m_tora = math_tora[i] if i < len(math_tora) else ""
    m_avrio = math_avrio[i] if i < len(math_avrio) else ""
    
    # Προσθήκη εικονιδίου αν υπάρχει μάθημα
    txt_tora = f"🔹 {m_tora}" if m_tora else ""
    txt_avrio = f"🔹 {m_avrio}" if m_avrio else ""
    
    html_table += f"<tr><td>{txt_tora}</td><td>{txt_avrio}</td></tr>"

html_table += "</table>"

# Εμφάνιση του πίνακα
st.markdown(html_table, unsafe_allow_html=True)

time.sleep(10)
st.rerun()
