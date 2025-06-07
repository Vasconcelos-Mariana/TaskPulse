import os
import json
from datetime import datetime

MAX_CHARS = 24
MAX_TAGS = 3

ID_FILE = "project_id_counter.txt"
PROJECTS_FILE = "projects.json"
TAGS_FILE = 'tags.json'

# ----- Project logic -----

def get_id():
    if os.path.exists(ID_FILE):
        with open(ID_FILE, 'r') as f:
            last_id = int(f.read().strip())
    else:
        last_id = 0
    new_id = last_id + 1
    with open(ID_FILE, "w") as f:
        f.write(str(new_id))
    return new_id

def fields_validation(name: str, description: str, tags: list[str]) -> bool:
    return bool(name.strip()) and bool(description.strip()) and len(tags) > 0

def save_project(project: dict):
    projects = []
    if os.path.exists(PROJECTS_FILE):
        with open(PROJECTS_FILE, 'r', encoding='utf-8') as f:
            try:
                projects = json.load(f)
            except json.JSONDecodeError:
                projects = []
            projects.append(project)
        with open(PROJECTS_FILE, "w", encoding="utf-8") as f:
            json.dump(projects, f, indent=4)

def create_project(name: str, description: str, tags: list[str], deadline: str = "") -> dict:
    if len(name) > MAX_CHARS:
        raise ValueError(f"Name must be at most {MAX_CHARS} characters.")
    if not fields_validation(name, description, tags):
        raise ValueError("Name, description and at least one tag are required.")

    project = {
        "id": get_id(),
        "name": name.strip(),
        "description": description.strip(),
        "tags": tags,
        "deadline": deadline.strip(),
        "created_at": datetime.now().isoformat()
    }

    save_project(project)
    return project

def load_existing_tags():
    if os.path.exists(TAGS_FILE):
        with open(TAGS_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_tag(tag: str):
    tags = load_existing_tags()
    if tag not in tags:
        tags.append(tag)
        with open(TAGS_FILE, "w", encoding="utf-8") as f:
            json.dump(tags, f, indent=4)

def suggest_tags(prefix: str):
    tags = load_existing_tags()
    return [tag for tag in tags if tag.lower().startswith(prefix.lower())]

def validate_tag_limit(current_tags: list[str]) -> bool:
    return len(current_tags) < MAX_TAGS

def peek_next_project_id():
    if os.path.exists(ID_FILE):
        with open(ID_FILE, "r") as f:
            last_id = int(f.read().strip())
    else:
        last_id = 0
    return last_id + 1

