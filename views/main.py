import customtkinter as ctk
from PIL import Image
import os

class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title('Time Manager')
        self.geometry('350x380')
        self.resizable(False,False)

        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('blue')

        self.build_ui()

    def build_ui(self):
        label_title = (ctk.CTkLabel(
            self,
            text = 'Time Manager',
            font = ctk.CTkFont("Arial Rounded MT Bold", size=40,weight='bold'),
            text_color = "#0f1317"
        ))
        label_title.pack(pady=(20, 10))

        start_button = ctk.CTkButton(
            self,
            text = "▶️Start Session",
            font = ctk.CTkFont('Calibri',size=20),
            fg_color = '#184852',
            hover_color = '#3c9971',
            width = 170,
            height = 35,
        )
        start_button.pack(pady=20)