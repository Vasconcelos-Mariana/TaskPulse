import customtkinter as ctk
from PIL import Image
import os
from views.new_project import NewProjectWindow
from views.view_projects import ViewProjectsWindow
from utils.ui import center_window



class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title('Time Manager')
        self.geometry(center_window(350, 380))
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

        new_button = ctk.CTkButton(button_row1, text="New Project",command=self.open_new_project, **button_style)
        new_button.pack(side="left", padx=10)

        view_button = ctk.CTkButton(button_row1, text="View Project",command=self.open_view_projects, **button_style)
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

        script_dir = os.path.dirname(os.path.abspath(__file__))
        gear_image_path = os.path.join(script_dir, "..", "utils", "engrenagem.png")
        gear_icon = ctk.CTkImage(
            light_image=Image.open(gear_image_path),
            dark_image=Image.open(gear_image_path),
            size=(24, 24)
        )

        settings_button = ctk.CTkButton(
            self,
            image=gear_icon,
            text="",
            width=40,
            height=40,
            fg_color="transparent",
            hover_color="#3d8491",
            border_width=0
        )
        settings_button.place(relx=0.99, rely=1, anchor="se")


        version_label = ctk.CTkLabel(
            self,
            text="   v 0.1.0",
            font=ctk.CTkFont("Calibri", size=12),
            text_color="#5a5a5a"
        )
        version_label.place(relx=0.01, rely=1, anchor="sw")

    def open_new_project(self):
        self.withdraw()
        NewProjectWindow(self)

    def open_view_projects(self):
        self.withdraw()
        ViewProjectsWindow(self)