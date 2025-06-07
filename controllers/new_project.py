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