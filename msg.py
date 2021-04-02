import pyautogui
import time

try:
    while True:
        time.sleep(0.5)
        pyautogui.typewrite('Good News\nBokhra Party Is BAck')
        time.sleep(0.5)
        pyautogui.press("enter")
except KeyboardInterrupt:
    print("Done")


