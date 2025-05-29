import os 

current_path = os.path.dirname(os.path.abspath(__file__))

BASE_PATH = os.path.sep.join(current_path.split(os.path.sep)[:-2] + ["temp"])

USER_FILE = os.path.join(BASE_PATH, "user.json")
