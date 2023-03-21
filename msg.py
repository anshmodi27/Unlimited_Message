import pyautogui
import time

try:
    while True:
        time.sleep(0.5)
        pyautogui.typewrite('Hello')
        time.sleep(0.5)
        pyautogui.press("enter")
except KeyboardInterrupt:
    print("Done")


