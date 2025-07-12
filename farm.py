import keyboard
import pygetwindow as gw
import time
import random
import threading
import json
import os
import sys

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")
if not os.path.exists(CONFIG_PATH):
    print("❌ HATA: config.json dosyası bulunamadı.")
    input("Devam etmek için Enter'a basın...")
    sys.exit(1)

with open(CONFIG_PATH) as f:
    config = json.load(f)

spam_keys = {k: v for k, v in config.items() if k in ['1', '2', '3', '4']}

movement_config = config.get("movement", {})
movement_keys = movement_config.get("enabled_keys", [])
move_press_duration = movement_config.get("duration_per_press", 0.2)
min_move_delay = movement_config.get("min_interval", 2)
max_move_delay = movement_config.get("max_interval", 5)

for key, val in spam_keys.items():
    if float(val) <= 0:
        print(f"❌ Hatalı interval: '{key}' için 0 veya negatif değer.")
        sys.exit(1)

target_window_name = "Rappelz"
running = False

def is_window_active(window_name):
    try:
        active_window = gw.getActiveWindow()
        return window_name.lower() in active_window.title.lower()
    except:
        return False

def spam_key_loop(key, interval):
    global running
    while True:
        if running and is_window_active(target_window_name):
            keyboard.press_and_release(key)
            time.sleep(interval)
        else:
            time.sleep(0.1)

def random_movement():
    global running
    while True:
        if running and is_window_active(target_window_name) and movement_keys:
            key = random.choice(movement_keys)
            keyboard.press(key)
            time.sleep(move_press_duration)
            keyboard.release(key)
            time.sleep(random.uniform(min_move_delay, max_move_delay))
        else:
            time.sleep(0.1)

def toggle_running():
    global running
    running = not running
    print("Spam STARTED" if running else "Spam STOPPED")

keyboard.add_hotkey('F8', toggle_running)

print(f"Spamming keys {list(spam_keys.keys())} at user-defined intervals.")
print(f"Random movement with keys: {movement_keys}")
print("Press F8 to start/stop spam.")

for key, interval in spam_keys.items():
    threading.Thread(target=spam_key_loop, args=(key, float(interval)), daemon=True).start()

threading.Thread(target=random_movement, daemon=True).start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nBot kapatıldı.")
