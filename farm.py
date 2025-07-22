import keyboard
import pygetwindow as gw
import time
import random
import threading
import json
import os
import sys
import pyautogui

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

# Mouse drag config (sabit değerler, istersen config.json'dan da alabilirsin)
mouse_drag_enabled = True
mouse_drag_ratio = 0.5  # pencerenin ortasından başla
mouse_drag_distance = 200  # piksel sağa/sola kaydır
mouse_drag_interval = 10   # kaç saniyede bir denesin
mouse_drag_direction = ["right", "left"]  # sağ/sol rastgele
mouse_drag_running = False

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

# Mouse drag fonksiyonu
def mouse_drag_window():
    global mouse_drag_running
    while True:
        if mouse_drag_running and is_window_active(target_window_name) and mouse_drag_enabled:
            try:
                win = None
                for w in gw.getWindowsWithTitle(target_window_name):
                    if w.isActive:
                        win = w
                        break
                if win:
                    # Pencere koordinatları
                    x = int(win.left + win.width * mouse_drag_ratio)
                    y = int(win.top + win.height * 0.5)
                    direction = random.choice(mouse_drag_direction)
                    dx = mouse_drag_distance if direction == "right" else -mouse_drag_distance
                    pyautogui.moveTo(x, y)
                    pyautogui.mouseDown(button='right')
                    pyautogui.moveRel(dx, 0, duration=0.3)
                    pyautogui.mouseUp(button='right')
                    print(f"Mouse drag: {direction} ({x},{y}) -> {dx} px")
                time.sleep(mouse_drag_interval)
            except Exception as e:
                print(f"Mouse drag hatası: {e}")
                time.sleep(2)
        else:
            time.sleep(0.5)

def toggle_running():
    global running
    running = not running
    print("Spam STARTED" if running else "Spam STOPPED")

# Mouse drag başlat/durdur
def toggle_mouse_drag():
    global mouse_drag_running
    mouse_drag_running = not mouse_drag_running
    print("Mouse drag STARTED" if mouse_drag_running else "Mouse drag STOPPED")

keyboard.add_hotkey('F8', toggle_running)
keyboard.add_hotkey('F9', toggle_mouse_drag)

print(f"Spamming keys {list(spam_keys.keys())} at user-defined intervals.")
print(f"Random movement with keys: {movement_keys}")
print("Press F8 to start/stop spam.")
print("Press F9 to start/stop mouse drag.")

for key, interval in spam_keys.items():
    threading.Thread(target=spam_key_loop, args=(key, float(interval)), daemon=True).start()

threading.Thread(target=random_movement, daemon=True).start()

threading.Thread(target=mouse_drag_window, daemon=True).start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nBot kapatıldı.")
