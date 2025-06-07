import os
import customtkinter as ctk

def center_window(width: int, height: int) -> str:
    import tkinter as tk
    root = tk.Tk()
    root.withdraw()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    return f"{width}x{height}+{x}+{y}"


class CustomConfirmDialog(ctk.CTkToplevel):
    def __init__(self, parent, title="Confirm Reset", message=""):
        super().__init__(parent)
        self.title(title)
        self.geometry(center_window(400, 180))
        self.resizable(False, False)
        self.grab_set()  # Modal

        self.result = None

        ctk.CTkLabel(self, text=message, wraplength=380, justify="left").pack(pady=(15, 10))

        self.entry = ctk.CTkEntry(self, placeholder_text="Type here...")
        self.entry.pack(padx=20, pady=(0, 10))
        self.entry.focus()  # foco no input ao abrir

        button_row = ctk.CTkFrame(self, fg_color="transparent")
        button_row.pack(pady=(5, 10))

        ctk.CTkButton(button_row, text="Ok", width=80, command=self.on_ok).pack(side="left", padx=10)
        ctk.CTkButton(button_row, text="Cancel", width=80, command=self.on_cancel).pack(side="left", padx=10)

# Enter as ok
        self.bind("<Return>", lambda event: self.on_ok())

    def on_ok(self):
        self.result = self.entry.get()
        self.destroy()

    def on_cancel(self):
        self.result = None
        self.destroy()


