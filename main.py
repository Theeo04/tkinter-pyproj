import tkinter as tk
from gui.add_transaction import AddTransactionWindow
from gui.view_transactions import ViewTransactionsWindow

class FinanceApp:
    def __init__(self):
        self.transactions = []  # Lista temporară pentru stocarea tranzacțiilor

    def start(self):
        root = tk.Tk()
        root.title("Aplicație Financiară")
        root.geometry("400x300")

        # Buton pentru adăugarea tranzacțiilor
        add_button = tk.Button(root, text="Adaugă Tranzacție", command=lambda: AddTransactionWindow(root, self.transactions))
        add_button.pack(pady=10)

        # Buton pentru vizualizarea tranzacțiilor
        view_button = tk.Button(root, text="Vizualizează Tranzacții", command=lambda: ViewTransactionsWindow(root, self.transactions))
        view_button.pack(pady=10)

        root.mainloop()


if __name__ == "__main__":
    app = FinanceApp()
    app.start()
