import tkinter as tk
from tkinter import messagebox
import json
import os

NOTES_FILE = "notes.json"

# Load notes from file
def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    return []

# Save notes to file
def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f)

# Add a new note
def add_note():
    note = text_input.get("1.0", tk.END).strip()
    if note:
        notes.append(note)
        save_notes(notes)
        update_list()
        text_input.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Empty Note", "Please write something first!")

# Delete selected note
def delete_note():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        notes.pop(index)
        save_notes(notes)
        update_list()
    else:
        messagebox.showwarning("No Selection", "Please select a note to delete.")

# Refresh the listbox
def update_list():
    listbox.delete(0, tk.END)
    for note in notes:
        listbox.insert(tk.END, note[:60] + ("..." if len(note) > 60 else ""))

# --- App Window ---
app = tk.Tk()
app.title("My Notes App")
app.geometry("500x450")
app.config(bg="#f5f5f5")

notes = load_notes()

# Title Label
tk.Label(app, text="📝 My Notes", font=("Arial", 18, "bold"), bg="#f5f5f5").pack(pady=10)

# Text input
text_input = tk.Text(app, height=5, width=55, font=("Arial", 11), bd=2, relief="groove")
text_input.pack(pady=5)

# Buttons
btn_frame = tk.Frame(app, bg="#f5f5f5")
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="➕ Add Note", command=add_note,
          bg="#4CAF50", fg="white", font=("Arial", 11), padx=10).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="🗑️ Delete Note", command=delete_note,
          bg="#f44336", fg="white", font=("Arial", 11), padx=10).grid(row=0, column=1, padx=5)

# Notes list
tk.Label(app, text="Saved Notes:", font=("Arial", 12, "bold"), bg="#f5f5f5").pack()

listbox = tk.Listbox(app, width=60, height=10, font=("Arial", 10), bd=2, relief="groove", selectbackground="#4CAF50")
listbox.pack(pady=5)

update_list()
app.mainloop()