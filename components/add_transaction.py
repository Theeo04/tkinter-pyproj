import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

class AddTransactionWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Adaugă Tranzacție")
        self.geometry("500x350")  # Dimensiunea fereastra mai mare
        self.resizable(False, False)

        # Creăm un canvas pentru a desena gradientul de fundal
        self.canvas = ctk.CTkCanvas(self, width=500, height=350, bg="#41a0db", bd=0, highlightthickness=0)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        # Creăm un fundal gradient (dacă dorești să fie o tranziție de culori)
        self.create_gradient()

        # Creăm etichetele (labels) cu text
        self.amount_label = self.create_label("Sumă:", 20, 60)
        self.date_label = self.create_label("Data (AAAA-LL-ZZ):", 20, 100)
        self.description_label = self.create_label("Descriere:", 20, 140)

        # Câmpuri pentru introducerea datelor
        self.amount_entry = ctk.CTkEntry(self, fg_color="white", width=220, font=("Arial", 12), text_color="black")  # Background alb și text negru
        self.amount_entry.place(x=250, y=60)  # Mutăm mai la dreapta

        self.date_entry = ctk.CTkEntry(self, fg_color="white", width=220, font=("Arial", 12), text_color="black")  # Background alb și text negru
        self.date_entry.place(x=250, y=100)  # Mutăm mai la dreapta

        self.description_entry = ctk.CTkEntry(self, fg_color="white", width=220, font=("Arial", 12), text_color="black")  # Background alb și text negru
        self.description_entry.place(x=250, y=140)  # Mutăm mai la dreapta

        # Buton pentru a adăuga tranzacția
        self.add_button = ctk.CTkButton(self, text="Adaugă", command=self.add_transaction)
        self.add_button.place(x=200, y=180)  # Poziționare centrata

    def create_label(self, text, x, y):
        """Metodă pentru a crea un label pe canvas cu text"""
        label = self.canvas.create_text(x, y, text=text, font=("Arial", 12, "bold"), anchor="w", fill="black")  # Text bold și negru
        return label

    def create_gradient(self):
        """Creează un fundal gradient pe canvas."""
        self.canvas.create_rectangle(0, 0, 500, 350, outline="", fill="#41a0db")
        # Poți adăuga efecte suplimentare pentru gradient, de exemplu:
        # gradiente personalizate folosind un algoritm sau biblioteca de imagini.

    def add_transaction(self):
        """Adaugă tranzacția într-o listă și închide fereastra."""
        amount = self.amount_entry.get()
        date = self.date_entry.get()
        description = self.description_entry.get()

        if not amount or not date or not description:
            messagebox.showerror("Eroare", "Toate câmpurile sunt obligatorii!")
            return

        # Aici poți salva tranzacția într-o bază de date sau într-un fișier
        transaction = {
            "amount": amount,
            "date": date,
            "description": description
        }
        # Adăugăm tranzacția într-o listă globală
        self.master.transactions.append(transaction)

        # Mesaj de succes
        messagebox.showinfo("Succes", "Tranzacția a fost adăugată!")
        print(transaction)

        # Închide fereastra de adăugare tranzacție
        self.destroy()
