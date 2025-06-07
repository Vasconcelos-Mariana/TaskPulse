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

        line_separator = ctk.CTkLabel(
            self,
            text = '',
            height = 1,
            width = 300,
            fg_color = "#cccccc"
        )
        line_separator.pack(pady=(0, 10))

        button_style = {
            "font": ctk.CTkFont("Calibri", size=17),
            "fg_color": "#4d7c85",
            "hover_color": "#3d8491",
            "width": 120,
            "height": 35
        }

        subtitle_projects = ctk.CTkLabel(
            self,
            text="Projects",
            font=ctk.CTkFont("Calibri", size=20),
            text_color="#0f1317"
        )
        subtitle_projects.pack(pady=1)

        button_row1 = ctk.CTkFrame(self,fg_color="transparent")
        button_row1.pack(pady=5)

        new_button = ctk.CTkButton(button_row1, text="New Project", **button_style)
        new_button.pack(side="left", padx=10)

        view_button = ctk.CTkButton(button_row1, text="View Project", **button_style)
        view_button.pack(side="left", padx=10)

        subtitle_statistics = ctk.CTkLabel(
            self,
            text="Statistics",
            font=ctk.CTkFont("Calibri", size=20),
            text_color="#0f1317"
        )
        subtitle_statistics.pack(pady=1)

        button_row = ctk.CTkFrame(self, fg_color="transparent")
        button_row.pack(pady=5)

        reports_button = ctk.CTkButton(button_row, text="Generate report", **button_style)
        reports_button.pack(side="left", padx=10)

        resume_button = ctk.CTkButton(button_row, text="Statistics", **button_style)
        resume_button.pack(side="left", padx=10)

