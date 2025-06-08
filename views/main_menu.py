import customtkinter as ctk
from PIL import Image
import os

class MainMenuFrame(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.place(relwidth=1, relheight=1)
        self.pack_propagate(False)
        self.configure(width=330, height=360)
        self.controller = controller
        self.build_ui()

    def build_ui(self):
        font_title = ctk.CTkFont("Arial Rounded MT Bold", size=40, weight="bold")
        font_subtitle = ctk.CTkFont("Calibri", size=20)
        font_button = ctk.CTkFont("Calibri", size=17)
        font_version = ctk.CTkFont("Calibri", size=12)

        button_style = {"font": font_button,"fg_color": "#4d7c85","hover_color": "#3d8491","width": 120,"height": 35}

        ctk.CTkLabel(self, text='Time Manager', font=font_title, text_color="#0f1317").pack(pady=(20, 10))

        ctk.CTkButton(
            self,
            text="▶️Start Session",
            font=ctk.CTkFont('Calibri', size=20),
            fg_color='#184852',
            hover_color='#3c9971',
            width=170,
            height=35,
            command=self.open_start_session
        ).pack(pady=20)

        ctk.CTkLabel(self, text='', height=1, width=300, fg_color="#cccccc").pack(pady=(0, 10))

        ctk.CTkLabel(self, text="Projects", font=font_subtitle, text_color="#0f1317").pack(pady=1)

        button_row1 = ctk.CTkFrame(self, fg_color="transparent")
        button_row1.pack(pady=5)
        ctk.CTkButton(button_row1, text="New Project", command=self.open_new_project, **button_style).pack(side="left", padx=10)
        ctk.CTkButton(button_row1, text="View Project", command=self.open_view_projects, **button_style).pack(side="left", padx=10)

        ctk.CTkLabel(self, text="Statistics", font=font_subtitle, text_color="#0f1317").pack(pady=1)

        button_row2 = ctk.CTkFrame(self, fg_color="transparent")
        button_row2.pack(pady=5)
        ctk.CTkButton(button_row2, text="Generate report", **button_style).pack(side="left", padx=10)
        ctk.CTkButton(button_row2, text="Statistics", **button_style).pack(side="left", padx=10)

        script_dir = os.path.dirname(os.path.abspath(__file__))
        gear_path = os.path.join(script_dir, "..", "utils", "engrenagem.png")
        if os.path.exists(gear_path):
            gear_icon = ctk.CTkImage(
                light_image=Image.open(gear_path),
                dark_image=Image.open(gear_path),
                size=(24, 24)
            )
            ctk.CTkButton(
                self,
                image=gear_icon,
                text="",
                width=40,
                height=40,
                fg_color="transparent",
                hover_color="#3d8491",
                border_width=0,
                command=self.open_settings
            ).place(relx=0.99, rely=1, anchor="se")

        ctk.CTkLabel(self, text="   v 0.1.0", font=font_version, text_color="#5a5a5a").place(relx=0.01, rely=1, anchor="sw")

# Navigation between frames

    def open_new_project(self):
        self.controller.show_frame("new_project")

    def open_view_projects(self):
        self.controller.show_frame("view_projects")

    def open_settings(self):
        self.controller.show_frame("settings")

    def open_start_session(self):
        self.controller.show_frame("start_session")
