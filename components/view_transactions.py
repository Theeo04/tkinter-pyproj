import sqlite3
from tkinter import ttk
import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class ViewTransactionsWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("500x400")
        self.title("Vizualizează Tranzacții")

        # Conexiunea la baza de date
        self.conn = sqlite3.connect("transactions.db")
        self.cursor = self.conn.cursor()

        self.create_widgets()

    def create_widgets(self):
        """Creează widgeturile pentru vizualizarea tranzacțiilor."""
        self.tree = ttk.Treeview(self, columns=("Date", "Description", "Amount"), show="headings")
        self.tree.heading("Date", text="Data")
        self.tree.heading("Description", text="Descriere")
        self.tree.heading("Amount", text="Sumă")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Buton pentru a deschide fereastra de grafice
        self.chart_button = ctk.CTkButton(self, text="Vizualizează Grafice", command=self.open_chart_window)
        self.chart_button.pack(pady=10)

        self.populate_table()

    def populate_table(self):
        """Populează tabelul cu tranzacțiile din baza de date."""
        try:
            self.cursor.execute("SELECT date, description, amount FROM transactions")
            transactions = self.cursor.fetchall()
            for transaction in transactions:
                self.tree.insert("", "end", values=transaction)
        except sqlite3.Error as e:
            print(f"Eroare la interogarea bazei de date: {e}")

    def open_chart_window(self):
        """Deschide o nouă fereastră pentru grafice."""
        ChartWindow(self)

    def __del__(self):
        """Închide conexiunea la baza de date când fereastra este distrusă."""
        if hasattr(self, "conn") and self.conn:
            self.conn.close()


class ChartWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("600x500")
        self.title("Grafice Tranzacții")

        # Crearea graficelor
        self.create_charts()

    def create_charts(self):
        """Creează graficele bazate pe datele tranzacțiilor."""
        conn = sqlite3.connect("transactions.db")
        cursor = conn.cursor()

        try:
            # Preluăm datele pentru grafic
            cursor.execute("SELECT date, SUM(amount) FROM transactions GROUP BY date")
            data = cursor.fetchall()
            dates = [row[0] for row in data]
            amounts = [row[1] for row in data]

            # Creăm un grafic cu matplotlib
            figure = Figure(figsize=(6, 4), dpi=100)
            ax = figure.add_subplot(111)
            ax.plot(dates, amounts, marker="o", linestyle="-", color="blue")
            ax.set_title("Sume tranzacționate per zi")
            ax.set_xlabel("Data")
            ax.set_ylabel("Sumă")

            # Integrarea graficului în Tkinter
            canvas = FigureCanvasTkAgg(figure, self)
            canvas.get_tk_widget().pack(fill="both", expand=True)
            canvas.draw()

        except sqlite3.Error as e:
            print(f"Eroare la generarea graficelor: {e}")
        finally:
            conn.close()
