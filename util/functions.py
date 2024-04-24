from datetime import date, datetime
from json import dump
from util.resources import users

def log(text: str):
    f = open("logs.txt", "a")
    f.write(f"[{date.today().strftime('%d/%m/%Y')} {datetime.now().strftime('%H:%M:%S')}] {text}\n")
    f.close()
    return

def logUser(user_id: int):
    if user_id not in users:
        users.append(user_id)
        with open("data.json", "w") as dataFile:
            dump({"users": users}, dataFile, indent=4)
        log(f"(INFO) New unique user! ({user_id})")
    return