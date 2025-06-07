import customtkinter as ctk
from views.main_menu import MainMenuFrame
from views.new_project import NewProjectFrame
from views.view_projects import ViewProjectsFrame
from views.settings import SettingsFrame
from views.settings import load_theme_preference
from views.start_session import StartSessionFrame
from views.timer import TimerFrame
from utils.ui import center_window

class AppController(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Time Manager')
        self.geometry(center_window(360,390))
        self.resizable(False, False)
        ctk.set_appearance_mode(load_theme_preference())

        self.frames = {}
        self.build_frames()
        self.show_frame("main")

    def build_frames(self):
        self.frames["main"] = MainMenuFrame(self, self)
        self.frames["new_project"] = NewProjectFrame(self, self)
        self.frames["view_projects"] = ViewProjectsFrame(self, self)
        self.frames["settings"] = SettingsFrame(self, self)
        self.frames["start_session"] = StartSessionFrame(self,self)
        self.frames["timer"] = TimerFrame(self,self)

        for frame in self.frames.values():
            frame.place_forget()

    def show_frame(self, name, **kwargs):
        frame = self.frames[name]
        frame.tkraise()

        if name == "timer" and "project" in kwargs:
            frame.start(kwargs["project"])

        self.frames[name].place(relx=0.5, rely=0.5, anchor="center")

        if hasattr(self.frames[name], "on_show"):
            self.frames[name].on_show()

