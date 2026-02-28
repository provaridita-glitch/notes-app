import streamlit as st
import json
import os

NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f)

st.title("📝 My Notes App")

notes = load_notes()

new_note = st.text_area("Write a new note:")
if st.button("➕ Add Note"):
    if new_note.strip():
        notes.append(new_note.strip())
        save_notes(notes)
        st.success("Note added!")
    else:
        st.warning("Please write something first!")

st.subheader("Saved Notes:")
for i, note in enumerate(notes):
    col1, col2 = st.columns([5, 1])
    col1.write(f"📌 {note}")
    if col2.button("🗑️", key=i):
        notes.pop(i)
        save_notes(notes)
        st.rerun()