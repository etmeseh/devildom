import keyboard
import pygetwindow as gw
import time
import random
import threading

# Target window name
target_window_name = "Rappelz"

# Ask user for spam intervals
def get_interval(key):
    while True:
        try:
            return float(input(f"Enter interval for key '{key}' (in seconds): "))
        except ValueError:
            print("Please enter a valid number.")

spam_keys = {
    '1': get_interval('1'),
    '2': get_interval('2'),
    '3': get_interval('3'),
    '4': get_interval('4')
}

# Movement settings
movement_keys = ['w', 'a', 's', 'd']
min_move_delay = 2
max_move_delay = 5
move_press_duration = 0.2

def is_window_active(window_name):
    try:
        active_window = gw.getActiveWindow()
        return window_name.lower() in active_window.title.lower()
    except:
        return False

def spam_key_loop(key, interval):
    while True:
        if is_window_active(target_window_name):
            keyboard.press_and_release(key)
        time.sleep(interval)

def random_movement():
    while True:
        if is_window_active(target_window_name):
            key = random.choice(movement_keys)
            keyboard.press(key)
            time.sleep(move_press_duration)
            keyboard.release(key)
        time.sleep(random.uniform(min_move_delay, max_move_delay))

print(f"\nSpamming keys {list(spam_keys.keys())} at user-defined intervals.")
print(f"Random movement with keys: {movement_keys}")

# Start threads for each spam key
for key, interval in spam_keys.items():
    threading.Thread(target=spam_key_loop, args=(key, interval), daemon=True).start()

# Start movement
threading.Thread(target=random_movement, daemon=True).start()

# Keep main thread alive
while True:
    time.sleep(1)
