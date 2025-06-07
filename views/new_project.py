import customtkinter as ctk
from tkinter import messagebox
from controllers import new_project as controller


class NewProjectWindow(ctk.CTkToplevel):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.selected_tags = []
        self.title("Creating New Project")
        self.geometry('330x350')
        self.build_ui()
        self.resizable(False, False)

    def validate_deadline_input(self, value: str) -> bool:
        if value == "":
            return True
        if value.count(",") > 1:
            return False
        return all(c.isdigit() or c == "," for c in value)

    def build_ui(self):
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.pack(pady=(10, 5), fill="x", padx=10)

        title_label = ctk.CTkLabel(header_frame, text="New Project", font=ctk.CTkFont(size=20))
        title_label.pack(side="left", padx=10)

# To push ID to top right
        ctk.CTkLabel(header_frame, text="").pack(side="left", expand=True)

# TESTING - Define ID before using it ???
        try:
            next_id = controller.peek_next_project_id()
        except Exception as e:
            print(f"[ERRO] Não foi possível obter ID: {e}")
            next_id = "?"

        id_label = ctk.CTkLabel(header_frame, text=f"ID: {next_id}", text_color="gray", font=ctk.CTkFont(size=10))
        id_label.pack(side="right")

        form_frame = ctk.CTkFrame(self, width=350, height=240)
        form_frame.pack(pady=5, padx=20)
        form_frame.grid_propagate(False)

# Name
        label_name = ctk.CTkLabel(form_frame, text="Name")
        label_name.grid(row=0, column=0, padx=(15, 5), pady=5, sticky="e")
        vcmd = self.register(lambda P: len(P) <= controller.MAX_CHARS)
        self.name_input = ctk.CTkEntry(
            form_frame,
            placeholder_text="Project name",
            width=180,
            validate="key",
            validatecommand=(vcmd, "%P"))
        self.name_input.grid(row=0, column=1, padx=(0, 10), pady=5, sticky="w")

# Description
        label_description = ctk.CTkLabel(form_frame, text="Description")
        label_description.grid(row=1, column=0, padx=(15, 5), pady=0, sticky="nw")
        self.description_input = ctk.CTkTextbox(
            form_frame,
            placeholder_text="Insert here your brief description for the project",
            width=180,
            height=80
        )
        self.description_input.grid(row=1, column=1, padx=(1, 5), pady=(2, 2), sticky="nw")

# Deadline
        vcmd_deadline = self.register(self.validate_deadline_input)
        label_deadline = ctk.CTkLabel(form_frame, text="Time limit")
        label_deadline.grid(row=2, column=0, padx=(15, 5), pady=5, sticky="nw")
        self.deadline_input = ctk.CTkEntry(
            form_frame,
            placeholder_text="in minutes",
            width=180,
        )
        self.deadline_input.grid(row=2, column=1, padx=(0, 5), pady=(2, 2), sticky="w")




