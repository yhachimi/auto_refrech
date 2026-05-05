import pyautogui
import time
from pynput import keyboard

running = True

def on_press(key):
    global running
    if key == keyboard.Key.esc:
        running = False
        return False

listener = keyboard.Listener(on_press=on_press)
listener.start()

while running:
    pyautogui.press("f5")
    pyautogui.press("down",30)
    time.sleep(6)
