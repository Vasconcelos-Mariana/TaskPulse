import customtkinter as ctk
from utils.ui import center_window
import json
import os
import tkinter.messagebox as msgbox
from utils.ui import CustomConfirmDialog


SETTINGS_FILE = os.path.join(os.path.dirname(__file__), "..", "settings.json")

class SettingsFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.pack_propagate(False)
        self.configure(width=330, height=360)
        self.controller = controller

        row = ctk.CTkFrame(self, fg_color="transparent")
        row.pack(pady=(20, 10))

        label = ctk.CTkLabel(row, text="Appearance Mode:")
        label.pack(side="left", padx=(5, 10))

        option = ctk.CTkOptionMenu(row, values=["Light", "Dark", "System"], command=self.change_mode)
        option.set(ctk.get_appearance_mode().capitalize())
        option.pack(side="left")

        back_button = ctk.CTkButton(self, text="Back", command=self.return_to_main)
        back_button.pack(pady=(5, 10))

        clear_button = ctk.CTkButton(
            self,
            text="Reset application data",
            fg_color="#aa4444",
            hover_color="#cc5555",
            command=self.confirm_reset
        )
        clear_button.pack(pady=(10, 10))

    def change_mode(self, value):
        ctk.set_appearance_mode(value.lower())
        save_theme_preference(value)

    def return_to_main(self):
        self.controller.show_frame("main")

    def confirm_reset(self):
        dialog = CustomConfirmDialog(
            self,
            message="⚠️ This will erase all saved projects, tags and counters.\n\nType 'Confirm' to proceed:",
            title="Confirm Reset"
        )
        self.wait_window(dialog)
        user_input = dialog.result

        if user_input is None:  # User cancelled
            return

        if user_input.strip() == "Confirm":
            reset_all_data()
            msgbox.showinfo("Done", "Application data has been reset.")

        else:
            msgbox.showerror("Error", "Confirmation failed. Please type 'Confirm' to proceed")



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

def reset_all_data():
    for file in ["projects.json", "tags.json", "project_id_counter.txt"]:
        path = os.path.join(os.path.dirname(__file__), "..", file)
        if os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                if path.endswith(".json"):
                    f.write("[]")
                else:
                    f.write("0")