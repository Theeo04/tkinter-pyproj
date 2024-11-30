from tkinter import ttk
import customtkinter as ctk

class ViewTransactionsWindow(ctk.CTkToplevel):
    def __init__(self, master, transactions):
        super().__init__(master)
        self.transactions = transactions
        self.geometry("500x350")
        self.title("Vizualizează Tranzacții")

        self.create_widgets()

    def create_widgets(self):
        """Creează widgeturile pentru vizualizarea tranzacțiilor."""
        self.tree = ttk.Treeview(self, columns=("Date", "Description", "Amount"), show="headings")
        self.tree.heading("Date", text="Data")
        self.tree.heading("Description", text="Descriere")
        self.tree.heading("Amount", text="Sumă")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.populate_table()

    def populate_table(self):
        """Populează tabelul cu tranzacțiile."""
        for transaction in self.transactions:
            self.tree.insert("", "end", values=transaction)
