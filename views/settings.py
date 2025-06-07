import customtkinter as ctk
from utils.ui import center_window
import json
import os

SETTINGS_FILE = os.path.join(os.path.dirname(__file__), "..", "settings.json")

class SettingsWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__()
        self.title("Settings")
        self.geometry(center_window(350, 380))
        self.resizable(False, False)

        row = ctk.CTkFrame(self, fg_color="transparent")
        row.pack(pady=(20, 10))

        label = ctk.CTkLabel(row, text="Appearance Mode:")
        label.pack(side="left", padx=(5, 10))

        option = ctk.CTkOptionMenu(row, values=["Light", "Dark", "System"], command=self.change_mode)
        option.set(ctk.get_appearance_mode().capitalize())
        option.pack(side="left")

        back_button = ctk.CTkButton(self, text="Back", command=self.return_to_main)
        back_button.pack(pady=(5, 10))

    def change_mode(self, value):
        ctk.set_appearance_mode(value.lower())
        save_theme_preference(value)

    def return_to_main(self):
        self.destroy()
        self.master.deiconify()

def save_theme_preference(theme: str):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump({"theme": theme.lower()}, f)

def load_theme_preference():
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("theme", "system")
        except json.JSONDecodeError:
            pass
    return "system"

