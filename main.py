import time
import pyautogui
import pyperclip

# Wait 5 seconds before starting
time.sleep(4)

# Press Tab once
pyautogui.press('tab')

# Press Arrow Down once
pyautogui.press('down')

# Press Tab 23 times
for _ in range(23):
    pyautogui.press('tab')
    pyautogui.press('down')


# Paste "Everything"
pyperclip.copy("Everything")
pyautogui.hotkey('ctrl', 'v')

# Press Tab
pyautogui.press('tab')

# Paste "Nothing"
pyperclip.copy("Nothing")
pyautogui.hotkey('ctrl', 'v')

# Press Tab
pyautogui.press('tab')

# Press Enter
pyautogui.press('enter')
