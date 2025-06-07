import customtkinter as ctk
from tkinter import messagebox
import os
import json
from controllers import new_project as controller


class ViewProjectsWindow(ctk.CTkToplevel):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.title("View Projects")
        self.geometry("400x420")
        self.resizable(False, False)

        self.build_ui()

    def build_ui(self):
        title = ctk.CTkLabel(self, text="All Projects", font=ctk.CTkFont(size=20, weight="bold"))
        title.pack(pady=(15, 10))

        self.scroll_frame = ctk.CTkScrollableFrame(self, width=370, height=300)
        self.scroll_frame.pack(pady=5, padx=10)

        self.load_projects()

        back_button = ctk.CTkButton(self, text="Main Menu", width=100, command=self.return_main_menu)
        back_button.pack(pady=10)

    def load_projects(self):
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        if not os.path.exists(controller.PROJECTS_FILE):
            ctk.CTkLabel(self.scroll_frame, text="No projects found.").pack(pady=10)
            return

        with open(controller.PROJECTS_FILE, "r", encoding="utf-8") as f:
            try:
                projects = json.load(f)
            except json.JSONDecodeError:
                ctk.CTkLabel(self.scroll_frame, text="Error reading project data.").pack(pady=10)
                return

        if not projects:
            ctk.CTkLabel(self.scroll_frame, text="No projects found.").pack(pady=10)
            return

        for project in projects:
            frame = ctk.CTkFrame(self.scroll_frame, fg_color="#f0f0f0")
            frame.pack(fill="x", pady=5, padx=5)

            title = ctk.CTkLabel(frame, text=f"{project['name']} (#{project['id']})", font=ctk.CTkFont(size=15, weight="bold"), text_color="#0f1317")
            title.pack(anchor="w", padx=10, pady=(5, 0))

            tags_text = ", ".join(project.get("tags", []))
            ctk.CTkLabel(frame, text=f"Tags: {tags_text}", font=ctk.CTkFont(size=12)).pack(anchor="w", padx=10)

            deadline = project.get("deadline", "")
            if deadline:
                ctk.CTkLabel(frame, text=f"Deadline: {deadline} min", font=ctk.CTkFont(size=12)).pack(anchor="w", padx=10)

            created = project.get("created_at", "")
            ctk.CTkLabel(frame, text=f"Created at: {created.split('T')[0]}", font=ctk.CTkFont(size=11), text_color="gray").pack(anchor="w", padx=10, pady=(0, 5))

    def return_main_menu(self):
        self.destroy()
        self.main_window.deiconify()
