import customtkinter as ctk
from views.main_menu import MainMenuFrame
from views.new_project import NewProjectFrame
from views.view_projects import ViewProjectsFrame
from views.settings import SettingsFrame

class AppController(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Time Manager')
        self.geometry("350x380")
        self.resizable(False, False)
        ctk.set_default_color_theme('blue')

        self.frames = {}
        self.build_frames()
        self.show_frame("main")

    def build_frames(self):
        self.frames["main"] = MainMenuFrame(self, self)
        self.frames["new_project"] = NewProjectFrame(self, self)
        self.frames["view_projects"] = ViewProjectsFrame(self, self)
        self.frames["settings"] = SettingsFrame(self, self)

        for frame in self.frames.values():
            frame.place_forget()

    def show_frame(self, name: str):
        if name not in self.frames:
            return

# Bug correction - hide all the frames so they won't show at the same time
        for frame in self.frames.values():
            frame.place_forget()

        self.frames[name].place(relx=0.5, rely=0.5, anchor="center")

        # Se o frame tiver método on_show, invoca-o
        if hasattr(self.frames[name], "on_show"):
            self.frames[name].on_show()

