import tkinter as tk
from tkinter import messagebox

class AddTransactionWindow:
    def __init__(self, master, transactions):
        self.transactions = transactions  # Referință la lista de tranzacții
        self.window = tk.Toplevel(master)
        self.window.title("Adaugă Tranzacție")
        self.window.geometry("300x200")

        # Data
        tk.Label(self.window, text="Data (YYYY-MM-DD):").pack()
        self.date_entry = tk.Entry(self.window)
        self.date_entry.pack()

        # Descriere
        tk.Label(self.window, text="Descriere:").pack()
        self.description_entry = tk.Entry(self.window)
        self.description_entry.pack()

        # Suma
        tk.Label(self.window, text="Sumă:").pack()
        self.amount_entry = tk.Entry(self.window)
        self.amount_entry.pack()

        # Buton pentru salvare
        save_button = tk.Button(self.window, text="Adaugă", command=self.save_transaction)
        save_button.pack(pady=10)

    def save_transaction(self):
        date = self.date_entry.get()
        description = self.description_entry.get()
        try:
            amount = float(self.amount_entry.get())
            self.transactions.append((date, description, amount))
            messagebox.showinfo("Succes", "Tranzacția a fost adăugată!")
            self.window.destroy()
        except ValueError:
            messagebox.showerror("Eroare", "Suma trebuie să fie un număr valid.")
