import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime
import sqlite3

class AddTransactionWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Adaugă Tranzacție")
        self.geometry("500x350")  # Dimensiunea fereastra mai mare
        self.resizable(False, False)

        # Conexiune la baza de date
        self.conn = sqlite3.connect("transactions.db")
        self.cursor = self.conn.cursor()

        # Creăm tabelul în caz că nu există
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                date DATE NOT NULL,
                description TEXT NOT NULL
            )
        """)
        self.conn.commit()

        # Creăm un canvas pentru a desena gradientul de fundal
        self.canvas = ctk.CTkCanvas(self, width=500, height=350, bg="#41a0db", bd=0, highlightthickness=0)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        # Creăm etichetele (labels) cu text
        self.amount_label = self.create_label("Sumă:", 20, 60)
        self.date_label = self.create_label("Data (AAAA-LL-ZZ):", 20, 100)
        self.description_label = self.create_label("Descriere:", 20, 140)

        # Câmpuri pentru introducerea datelor
        self.amount_entry = ctk.CTkEntry(self, fg_color="white", width=220, font=("Arial", 12), text_color="black")
        self.amount_entry.place(x=250, y=60)

        self.date_entry = ctk.CTkEntry(self, fg_color="white", width=220, font=("Arial", 12), text_color="black")
        self.date_entry.place(x=250, y=100)

        self.description_entry = ctk.CTkEntry(self, fg_color="white", width=220, font=("Arial", 12), text_color="black")
        self.description_entry.place(x=250, y=140)

        # Buton pentru a adăuga tranzacția
        self.add_button = ctk.CTkButton(self, text="Adaugă", command=self.add_transaction)
        self.add_button.place(x=200, y=180)

    def create_label(self, text, x, y):
        """Metodă pentru a crea un label pe canvas cu text"""
        label = self.canvas.create_text(x, y, text=text, font=("Arial", 12, "bold"), anchor="w", fill="black")
        return label

    def add_transaction(self):
        """Adaugă tranzacția în baza de date"""
        amount = self.amount_entry.get()
        date = self.date_entry.get()
        description = self.description_entry.get()

        if not amount or not date or not description:
            messagebox.showerror("Eroare", "Toate câmpurile sunt obligatorii!")
            return

        try:
            # Validăm și formăm data ca text în formatul `YYYY-MM-DD`
            parsed_date = datetime.strptime(date, "%Y-%m-%d").date()

            # Inserăm tranzacția în baza de date
            self.cursor.execute("""
                INSERT INTO transactions (amount, date, description)
                VALUES (?, ?, ?)
            """, (float(amount), str(parsed_date), description))
            self.conn.commit()

            # Mesaj de succes
            messagebox.showinfo("Succes", "Tranzacția a fost adăugată!")
            print(f"Tranzacție adăugată: {amount}, {parsed_date}, {description}")

            # Închide fereastra de adăugare tranzacție
            self.destroy()
        except ValueError:
            messagebox.showerror("Eroare", "Data trebuie să fie în formatul corect: AAAA-LL-ZZ")

    def __del__(self):
        """Închide conexiunea la baza de date când fereastra este distrusă"""
        if hasattr(self, "conn") and self.conn:
            self.conn.close()
