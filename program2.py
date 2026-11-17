import json
import os
FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "capitals.json")
if os.path.exists(FILE):
    with open(FILE, encoding="utf-8") as f:
        d = json.load(f)
else:
    d = {"Ukraine": "Kyiv", "France": "Paris", "Germany": "Berlin"}
while True:
    c = input("\n1-додати 2-пошук 3-видалити 0-вихід: ")
    if c == "1":
        d[input("Країна: ").strip()] = input("Столиця: ").strip()
    elif c == "2":
        x = input("Країна або столиця: ").strip().lower()
        res = [f"{k} - {v}" for k, v in d.items() if x in (k.lower(), v.lower())]
        print("\n".join(res) or "Не знайдено")
    elif c == "3":
        k = input("Країна для видалення: ").strip()
        print("Видалено" if d.pop(k, None) else "Такої країни немає")
    elif c == "0":
        break
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=4)