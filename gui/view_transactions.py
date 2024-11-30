import tkinter as tk
from tkinter import ttk

class ViewTransactionsWindow:
    def __init__(self, master, transactions):
        self.transactions = transactions  # Referință la lista de tranzacții
        self.window = tk.Toplevel(master)
        self.window.title("Tranzacții")
        self.window.geometry("400x300")

        # Configurare tabel
        self.tree = ttk.Treeview(self.window, columns=("Date", "Description", "Amount"), show="headings")
        self.tree.heading("Date", text="Data")
        self.tree.heading("Description", text="Descriere")
        self.tree.heading("Amount", text="Sumă")

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Populare tabel
        self.populate_table()

    def populate_table(self):
        for transaction in self.transactions:
            self.tree.insert("", tk.END, values=transaction)
