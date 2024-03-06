from datetime import date, datetime

def log(text):
    f = open("logs.txt", "a")
    f.write(f"[{date.today().strftime('%d/%m/%Y')} {datetime.now().strftime('%H:%M:%S')}] {text}\n")
    f.close()
    return