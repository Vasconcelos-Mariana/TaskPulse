
import customtkinter as ctk
from tkinter import messagebox
from controllers import new_project as controller


class NewProjectFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.selected_tags = []
        self.build_ui()

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

        next_id = controller.peek_next_project_id()
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
            validate="key",
            validatecommand=(vcmd_deadline, "%P"),
            width=180,
        )
        self.deadline_input.grid(row=2, column=1, padx=(0, 5), pady=(2, 2), sticky="w")

# Tags
        label_tags = ctk.CTkLabel(form_frame, text="Tags")
        label_tags.grid(row=3, column=0, padx=(15, 5), pady=5, sticky="nw")

        tag_row_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        tag_row_frame.grid(row=3, column=1, padx=(0, 5), pady=5, sticky="nw")

        self.nova_tag_input = ctk.CTkEntry(tag_row_frame, placeholder_text="New tag", width=120)
        self.nova_tag_input.pack(side="left", padx=(0, 5), pady=0)
        self.nova_tag_input.bind("<KeyRelease>", self.on_tag_input)

        self.btn_add_tag = ctk.CTkButton(tag_row_frame, text="Add", fg_color="#4d7c85", width=50, command=self.add_tag)
        self.btn_add_tag.pack(side="left", pady=0)

        self.suggestions_label = ctk.CTkLabel(form_frame, text="", text_color="gray")
        self.suggestions_label.grid(row=4, column=1, sticky="w", padx=5)

        self.tags_display_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        self.tags_display_frame.grid(row=4, column=1, sticky="w", padx=5, pady=(2, 2))

# End button

        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=10, fill="x")

        inner_frame = ctk.CTkFrame(button_frame, fg_color="transparent")
        inner_frame.pack()

        back_button = ctk.CTkButton(
            inner_frame,
            text="Main menu",
            fg_color="#4d7c85",
            hover_color="#3d8491",
            command=self.main_menu,
            width=100
        )
        back_button.pack(side="left", padx=25)

        create_button = ctk.CTkButton(
            inner_frame,
            text="Create Project",
            fg_color="#4d7c85",
            hover_color="#3d8491",
            command=self.create_project,
            width=100
        )
        create_button.pack(side="left", padx=22)

# Tag function .
    def on_tag_input(self, event):
        prefix = self.nova_tag_input.get().strip()
        if not prefix:
            self.suggestions_label.configure(text="")
            return
        suggestions = controller.suggest_tags(prefix)
        self.suggestions_label.configure(text=", ".join(suggestions[:3]) if suggestions else "No suggestions")

    def add_tag(self):
        tag = self.nova_tag_input.get().strip()
        if not tag:
            return
        if tag in self.selected_tags:
            messagebox.showwarning("Warning", "Tag already added.")
            return
        if not controller.validate_tag_limit(self.selected_tags):
            messagebox.showerror("Error", "Limit of 3 tags per project")
            return

        self.selected_tags.append(tag)
        controller.save_tag(tag)
        self.nova_tag_input.delete(0, "end")
        self.suggestions_label.configure(text="")

        for widget in self.tags_display_frame.winfo_children():
            widget.destroy()
        for t in self.selected_tags:
            tag_label = ctk.CTkLabel(self.tags_display_frame, text=t, fg_color="#ddddff", text_color="black", corner_radius=5, padx=6)
            tag_label.pack(side="left", padx=2)

    def create_project(self):
        name = self.name_input.get().strip()
        description = self.description_input.get("1.0", "end-1c").strip()
        deadline = self.deadline_input.get().strip()
        try:
            project = controller.create_project(name, description, self.selected_tags, deadline)
            messagebox.showinfo("Success", f"Project '{project['name']}' created.")
            self.main_menu()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def main_menu(self):
        self.controller.show_frame("main")

