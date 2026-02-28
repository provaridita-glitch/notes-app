import streamlit as st
import json
import os
from datetime import datetime

NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f)

st.title("✨ Provaridita's Notes App")
st.caption("Your personal notes — write, save and delete anytime!")

notes = load_notes()

new_note = st.text_area("Write a new note:", max_chars=500)
st.caption(f"Characters used: {len(new_note)}/500")

if st.button("➕ Add Note"):
    if new_note.strip():
        timestamp = datetime.now().strftime("%d %b %Y, %I:%M %p")
        notes.append(f"[{timestamp}] {new_note.strip()}")
        save_notes(notes)
        st.success("Note added!")
    else:
        st.warning("Please write something first!")

st.subheader(f"Saved Notes: ({len(notes)} total)")
for i, note in enumerate(notes):
    col1, col2 = st.columns([5, 1])
    col1.write(f"📌 {note}")
    if col2.button("🗑️", key=i):
        notes.pop(i)
        save_notes(notes)
        st.rerun()