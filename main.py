from views.main import MainWindow
from views.settings import load_theme_preference
import customtkinter as ctk

ctk.set_appearance_mode(load_theme_preference())

if __name__=='__main__':
    app = MainWindow()
    app.mainloop()