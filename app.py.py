import tkinter as tk
from tkinter import messagebox
import datetime
import os
import tempfile

root = tk.Tk()
root.title("ব্র্যাক ব্যাংক - ক্যাশ ডিপোজিট ভাউচার")
root.geometry("480x750")
root.configure(bg="#f4f6f9")
root.resizable(False, False)

# হেডার
header_frame = tk.Frame(root, bg="#f4f6f9")
header_frame.pack(fill="x", pady=(10, 5))

tk.Label(header_frame, text="ব্র্যাক ব্যাংক", font=("Arial", 16, "bold"), fg="#003366", bg="#f4f6f9").pack()
tk.Label(header_frame, text="সিংগাশোলপুর এজেন্ট ব্যাংকিং আউটলেট, নড়াইল।", font=("Arial", 10, "bold"), fg="#333333", bg="#f4f6f9").pack()
tk.Label(header_frame, text="ক্যাশ ডিপোজিট ভাউচার (A5)", font=("Arial", 9), fg="#666666", bg="#f4f6f9").pack()

# গ্রাহক ও হিসাবের তথ্য
info_frame = tk.LabelFrame(root, text=" গ্রাহক ও হিসাবের তথ্য ", font=("Arial", 9, "bold"), bg="#ffffff", padx=10, pady=8)
info_frame.pack(fill="x", padx=15, pady=5)

tk.Label(info_frame, text="তারিখ:", bg="#ffffff").grid(row=0, column=0, sticky="w", pady=2)
date_entry = tk.Entry(info_frame, width=24)
date_entry.insert(0, datetime.datetime.now().strftime("%d/%m/%Y"))
date_entry.grid(row=0, column=1, pady=2)

tk.Label(info_frame, text="হিসাবধারীর নাম:", bg="#ffffff").grid(row=1, column=0, sticky="w", pady=2)
name_entry = tk.Entry(info_frame, width=24)
name_entry.grid(row=1, column=1, pady=2)

tk.Label(info_frame, text="একাউন্ট নম্বর:", bg="#ffffff").grid(row=2, column=0, sticky="w", pady=2)
acc_entry = tk.Entry(info_frame, width=24)
acc_entry.grid(row=2, column=1, pady=2)

tk.Label(info_frame, text="মোবাইল নম্বর:", bg="#ffffff").grid(row=3, column=0, sticky="w", pady=2)
mob_entry = tk.Entry(info_frame, width=24)
mob_entry.grid(row=3, column=1, pady=2)

# নোট টেবিল
notes = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
note_entries = {}
note_totals = {}

table_frame = tk.Frame(root, bg="#ffffff", bd=1, relief="solid")
table_frame.pack(fill="x", padx=15, pady=8)

table_frame.columnconfigure(0, weight=1)
table_frame.columnconfigure(1, weight=1)
table_frame.columnconfigure(2, weight=1)

tk.Label(table_frame, text="টাকা", bg="#d0e1fd", font=("Arial", 9, "bold"), bd=1, relief="ridge").grid(row=0, column=0, sticky="nsew", ipady=3)
tk.Label(table_frame, text="নোট সংখ্যা", bg="#fce4ec", fg="#d32f2f", font=("Arial", 9, "bold"), bd=1, relief="ridge").grid(row=0, column=1, sticky="nsew", ipady=3)
tk.Label(table_frame, text="মোট টাকা", bg="#e8f5e9", font=("Arial", 9, "bold"), bd=1, relief="ridge").grid(row=0, column=2, sticky="nsew", ipady=3)

grand_total_var = tk.StringVar(value="0")

def calculate(event=None):
    total = 0
    for n in notes:
        txt = note_entries[n].get().strip()
        qty = int(txt) if txt.isdigit() else 0
        sub = n * qty
        note_totals[n].config(text=str(sub))
        total += sub
    grand_total_var.set(str(total))

for i, note in enumerate(notes, start=1):
    tk.Label(table_frame, text=str(note), bg="#e3f2fd", bd=1, relief="groove", font=("Arial", 9)).grid(row=i, column=0, sticky="nsew")
    
    ent = tk.Entry(table_frame, justify="center", bg="#fff0f5", relief="groove", font=("Arial", 9))
    ent.grid(row=i, column=1, sticky="nsew")