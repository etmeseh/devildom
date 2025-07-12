import tkinter as tk
from tkinter import messagebox
import json
import os

root = tk.Tk()
root.title("Rappelz Otomatik Tuş Botu — Ayar Paneli")
root.geometry("400x600")

tk.Label(root, text="Tuş Aralıklarını Girin (saniye)", font=("Segoe UI", 11, "bold")).pack(pady=10)

keys = ['1', '2', '3', '4']
entries = {}

for key in keys:
    tk.Label(root, text=f"Tuş {key}").pack()
    entry = tk.Entry(root)
    entry.insert(0, "1")
    entry.pack()
    entries[key] = entry

# Hareket ayarları
tk.Label(root, text="Hareket Tuşları (W, A, S, D)", font=("Segoe UI", 11, "bold")).pack(pady=15)
movement_vars = {}
for key in ['w', 'a', 's', 'd']:
    var = tk.BooleanVar(value=True)
    cb = tk.Checkbutton(root, text=f"{key.upper()} yönüne git", variable=var)
    cb.pack()
    movement_vars[key] = var

tk.Label(root, text="Her tuşa basma süresi (sn)").pack()
duration_entry = tk.Entry(root)
duration_entry.insert(0, "0.4")
duration_entry.pack()

tk.Label(root, text="Min bekleme süresi (sn)").pack()
min_delay_entry = tk.Entry(root)
min_delay_entry.insert(0, "3")
min_delay_entry.pack()

tk.Label(root, text="Max bekleme süresi (sn)").pack()
max_delay_entry = tk.Entry(root)
max_delay_entry.insert(0, "7")
max_delay_entry.pack()

def save_config():
    config = {}
    for key in keys:
        try:
            val = float(entries[key].get())
            if val <= 0:
                raise ValueError
            config[key] = val
        except ValueError:
            messagebox.showerror("Hatalı Giriş", f"Tuş {key} için 0'dan büyük sayı girin.")
            return

    try:
        duration = float(duration_entry.get())
        min_d = float(min_delay_entry.get())
        max_d = float(max_delay_entry.get())
        if duration <= 0 or min_d < 0 or max_d < 0 or min_d > max_d:
            raise ValueError
    except ValueError:
        messagebox.showerror("Hatalı Giriş", "Geçerli hareket süreleri girin.")
        return

    config["movement"] = {
        "enabled_keys": [k for k, v in movement_vars.items() if v.get()],
        "duration_per_press": duration,
        "min_interval": min_d,
        "max_interval": max_d
    }

    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)

    messagebox.showinfo("Başarılı", "Ayarlar kaydedildi.")

tk.Button(root, text="Kaydet", command=save_config).pack(pady=20)
root.mainloop()
