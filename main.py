import customtkinter as ctk
from components.navbar import Navbar
from PIL import Image, ImageTk  # Pentru a lucra cu imaginile și a le converte în PhotoImage
from components.add_transaction import AddTransactionWindow  # Importă fereastra de adăugare tranzacție

class FinanceApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Aplicație Financiară")
        self.geometry("900x600")
        ctk.set_appearance_mode("dark")  # Mod întunecat
        ctk.set_default_color_theme("blue")  # Tema de culoare

        # Setează canvas-ul pentru imaginea de fundal
        self.canvas = ctk.CTkCanvas(self)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)  # Fă canvas-ul să ocupe toată fereastra

        # Imaginea de fundal
        self.bg_image = Image.open("utils/background_mainpage.png")  # Înlocuiește cu calea corectă

        # Actualizează imaginea de fundal la dimensiunea ferestrei
        self.update_background()

        # Creează navbar-ul
        self.navbar = Navbar(self, self.open_add_window, self.open_view_window)

        # Butonul "Ieșire" în dreapta jos
        self.exit_button = ctk.CTkButton(self, text="Ieșire", command=self.quit, fg_color="#e74c3c", width=150)
        self.exit_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

        # Ascultă evenimentul de redimensionare pentru a actualiza imaginea
        self.bind("<Configure>", self.on_resize)

        # Inițializare listă pentru tranzacții
        self.transactions = []

    def on_resize(self, event):
        """Actualizează imaginea de fundal când fereastra este redimensionată."""
        self.update_background()

    def update_background(self):
        """Actualizează imaginea de fundal pentru a se potrivi cu dimensiunile ferestrei."""
        window_width = self.winfo_width()
        window_height = self.winfo_height()

        # Redimensionăm imaginea pentru a se potrivi ferestrei
        bg_resized = self.bg_image.resize((window_width, window_height))
        self.bg_image_tk = ImageTk.PhotoImage(bg_resized)

        # Șterge imaginea existentă pe canvas și adaugă imaginea redimensionată
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.bg_image_tk, anchor="nw")

        # Adăugăm textul pe canvas (după ce imaginea a fost actualizată)
        self.create_text()

    def create_text(self):
        """Adaugă textul pe canvas cu padding la stânga."""

        padding_left = 35  
        self.canvas.create_text(400 + padding_left, 200, text="Bine ai venit în aplicația ta financiară!", font=("Arial", 30, "bold"), fill="white")

    def open_add_window(self):
        """Deschide fereastra pentru adăugarea tranzacțiilor."""
        AddTransactionWindow(self)

    def open_view_window(self):
        """Deschide fereastra pentru vizualizarea tranzacțiilor."""
        print("Deschide fereastra pentru Vizualizează Tranzacții")

if __name__ == "__main__":
    app = FinanceApp()
    app.mainloop()
