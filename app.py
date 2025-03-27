import time
import pyautogui

while True:
    time.sleep(5)

    # Move mouse in a pattern
    for i in range(50):
        pyautogui.moveTo(i * 10, 5)
    pyautogui.press('ctrl')

    for i in range(50):
        pyautogui.moveTo(5, (50 - i) * 10)

    pyautogui.hotkey('alt', 'tab')  # Switch window

    for i in range(2):
        time.sleep(2)
        pyautogui.hotkey('win', 'd')  # Show Desktop

    for i in range(2):
        time.sleep(2)
        pyautogui.press('win')  # Open Start Menu

    # Open a new browser tab
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)

    # Type "Microsoft Learn" and search
    pyautogui.write('Microsoft Learn', interval=0.1)
    pyautogui.press('enter')
    time.sleep(3)  # Wait for page to load

    # Scroll down and up
    for _ in range(3):
        pyautogui.scroll(-500)  # Scroll down
        time.sleep(1)

    for _ in range(3):
        pyautogui.scroll(500)  # Scroll up
        time.sleep(1)

    # Close the tab
    pyautogui.hotkey('ctrl', 'w')

    time.sleep(10)  # Wait before repeating the loop
