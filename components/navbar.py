import customtkinter as ctk

class Navbar(ctk.CTkFrame):
    def __init__(self, master, open_add_window, open_view_window):
        super().__init__(master, height=50, corner_radius=0, fg_color="#4061ae")  # Fundal navbar albastru
        self.pack(fill="x", side="top")

        # Font pentru textul butoanelor
        button_font = ctk.CTkFont(size=14, weight="bold")  # Font mai mare și bold

        # Frame pentru partea stângă a navbar-ului
        self.left_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.left_frame.pack(side="left", padx=15, pady=15)

        # Frame pentru partea dreaptă a navbar-ului
        self.right_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.right_frame.pack(side="right", padx=15, pady=15)

        # Buton "Adaugă Tranzacție" în stânga
        self.add_button = ctk.CTkButton(
            self.left_frame,
            text="Adaugă Tranzacție",
            command=open_add_window,
            width=150,
            fg_color="#242424",  # Fundal negru
            font=button_font  # Aplica fontul personalizat
        )
        self.add_button.pack(pady=5)

        # Buton "Vizualizează Tranzacții" în dreapta
        self.view_button = ctk.CTkButton(
            self.right_frame,
            text="Vizualizează Tranzacții",
            command=open_view_window,
            width=150,
            fg_color="#242424",  # Fundal negru
            font=button_font  # Aplica fontul personalizat
        )
        self.view_button.pack(pady=5)
