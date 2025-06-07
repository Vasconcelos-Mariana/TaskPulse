import customtkinter as ctk
from controllers import start_session as controller


class StartSessionFrame(ctk.CTkFrame):
    def __init__(self, parent, app_controller):
        super().__init__(parent)
        self.app_controller = app_controller
        self.projects = []
        self.build_ui()

    def build_ui(self):
        title_label = ctk.CTkLabel(self, text="Start Session", font=ctk.CTkFont(size=24, weight="bold"))
        title_label.pack(pady=(15, 10))

        self.scroll_frame = ctk.CTkScrollableFrame(self, width=300, height=220)
        self.scroll_frame.pack(padx=20, pady=5, fill="both", expand=False)

        self.refresh_project_list()

        back_button = ctk.CTkButton(self, text="Back to menu", command=self.go_back, fg_color="#4d7c85", hover_color="#3d8491")
        back_button.pack(pady=10)

    def refresh_project_list(self):
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        self.projects = controller.get_all_projects()

        if not self.projects:
            empty_label = ctk.CTkLabel(self.scroll_frame, text="No projects found.", text_color="gray")
            empty_label.pack(pady=10)
            return

        for project in self.projects:
            frame = ctk.CTkFrame(self.scroll_frame, fg_color="transparent")
            frame.pack(fill="x", pady=5, padx=5)

            label = ctk.CTkLabel(frame, text=f"#{project['id']}  {project['name']}", anchor="w")
            label.pack(side="left", fill="x", expand=True, padx=(5, 10))

            start_btn = ctk.CTkButton(frame, text="Start", width=60, command=lambda p=project: self.start_timer(p))
            start_btn.pack(side="right")

    def start_timer(self, project):
        controller.start_session(project)
        self.app_controller.show_frame("timer", project=project)

    def go_back(self):
        self.app_controller.show_frame("main")
