import customtkinter as ctk
import datetime
from tkinter import messagebox
import json
import os


class TimerFrame(ctk.CTkFrame):
    def __init__(self, parent, app_controller):
        super().__init__(parent)
        self.app_controller = app_controller
        self.project = None
        self.elapsed_seconds = 0
        self.timer_running = False
        self.after_id = None
        self.build_ui()

    def build_ui(self):
        self.main_frame = ctk.CTkFrame(self, corner_radius=12)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.title_label = ctk.CTkLabel(self.main_frame, text="", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.pack(pady=(15, 5))

        self.time_display = ctk.CTkLabel(self.main_frame, text="00:00:00", font=ctk.CTkFont(size=38, weight="bold"))
        self.time_display.pack(pady=(5, 5))

        self.progress_label = ctk.CTkLabel(self.main_frame, text="0%", font=ctk.CTkFont(size=16))
        self.progress_label.pack(pady=(5, 5))

        self.progress_bar = ctk.CTkProgressBar(self.main_frame, width=240)
        self.progress_bar.pack(pady=(5, 15))
        self.progress_bar.set(0)

        self.button_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.button_frame.pack(pady=(5, 5))

        self.toggle_button = ctk.CTkButton(self.button_frame, text="Start", command=self.toggle_timer, width=80)
        self.toggle_button.pack(side="left", padx=5)

        self.stop_button = ctk.CTkButton(self.button_frame, text="Stop", fg_color="#c94c4c", hover_color="#a23c3c",command=self.stop_timer, width=80)
        self.stop_button.pack(side="left", padx=5)

        self.cancel_button = ctk.CTkButton(self.main_frame, text="Cancel", command=self.return_to_project_selection)
        self.cancel_button.pack(pady=(10, 0))

    def start(self, project):
        self.project = project
        self.elapsed_seconds = 0
        self.timer_running = False
        self.progress_bar.set(0)
        self.update_time_display()
        self.update_progress()
        self.title_label.configure(text=f"Project: {project['name']} (#{project['id']})")
        self.toggle_button.configure(text="Start")

    def count_up(self):
        if self.timer_running:
            self.elapsed_seconds += 1
            self.update_progress()

            self.after_id = self.after(1000, self.count_up)

    def update_progress(self):
        try:
            total_seconds = int(self.project.get("deadline", "0").strip()) * 60
        except ValueError:
            total_seconds = 0

        if total_seconds == 0:
            self.progress_bar.set(0)
            self.progress_label.configure(text="∞ (no deadline)")
            return

        percent = (self.elapsed_seconds / total_seconds) * 100
        progress = min(percent / 100, 1.0)
        self.progress_bar.set(progress)

        if self.elapsed_seconds <= total_seconds:
            self.progress_label.configure(text=f"{int(percent)}%")
        else:
            overtime_seconds = self.elapsed_seconds - total_seconds
            minutes = overtime_seconds // 60
            seconds = overtime_seconds % 60

            if minutes < 60:
                overtime_str = f"+{minutes} min"
            else:
                hours = minutes // 60
                rem_minutes = minutes % 60
                overtime_str = f"+{hours}h{rem_minutes:02}"

            self.progress_label.configure(text=f"{int(percent)}%  (Overtime {overtime_str})")

    def toggle_timer(self):
        if not self.timer_running and self.elapsed_seconds == 0:
            # first time initiating the session
            self.timer_running = True
            self.count_up()
            self.toggle_button.configure(text="Pause")

        elif self.timer_running:
            # Pause
            self.timer_running = False
            if self.after_id:
                self.after_cancel(self.after_id)
                self.after_id = None
            self.toggle_button.configure(text="Resume")

        else:
            # Resume
            self.timer_running = True
            self.toggle_button.configure(text="Pause")
            self.count_up()

    def stop_timer(self):
        if self.after_id:
            self.after_cancel(self.after_id)
            self.after_id = None
        self.timer_running = False
        self.toggle_button.configure(text="Start")

        duration = self.elapsed_seconds
        self.save_session(duration)
        messagebox.showinfo("Session ended", f"Session of {duration // 60} min {duration % 60} sec saved.")
        self.return_to_project_selection()

    def return_to_project_selection(self):
        if self.after_id:
            self.after_cancel(self.after_id)
            self.after_id = None
        self.timer_running = False
        self.toggle_button.configure(text="Start")
        self.app_controller.show_frame("start_session")

    def save_session(self, duration):
        session = {
            "start_time": datetime.datetime.now().isoformat(),
            "duration_seconds": duration
        }

        path = "projects.json"
        if not os.path.exists(path):
            return

        with open(path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return

        for p in data:
            if p["id"] == self.project["id"]:
                p.setdefault("sessions", []).append(session)
                break

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def count_up(self):
        if self.timer_running:
            self.elapsed_seconds += 1
            self.update_time_display()
            self.update_progress()
            self.after_id = self.after(1000, self.count_up)

    def update_time_display(self):
        hours = self.elapsed_seconds // 3600
        minutes = (self.elapsed_seconds % 3600) // 60
        seconds = self.elapsed_seconds % 60
        self.time_display.configure(text=f"{hours:02}:{minutes:02}:{seconds:02}")