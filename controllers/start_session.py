import json
import os
from datetime import datetime

PROJECTS_FILE = "projects.json"

def get_all_projects():
    if os.path.exists(PROJECTS_FILE):
        with open(PROJECTS_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def start_session(project):
    project["session_active"] = True
    project["start_time"] = datetime.now().isoformat()
    project["elapsed"] = 0

    all_projects = get_all_projects()

#Update project on the list
    for i, p in enumerate(all_projects):
        if p["id"] == project["id"]:
            all_projects[i] = project
            break

#Saving it
    with open(PROJECTS_FILE, "w", encoding="utf-8") as f:
        json.dump(all_projects, f, indent=4)
