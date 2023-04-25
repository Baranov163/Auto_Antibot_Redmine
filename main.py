import time
import pyautogui

pyautogui.hotkey('win', 'r')
pyautogui.typewrite('powershell')
pyautogui.press('enter')
time.sleep(1)
pyautogui.typewrite('cd .ssh')
pyautogui.press('enter')
pyautogui.typewrite('ssh test-postgres01-nd')
pyautogui.press('enter')
pyautogui.typewrite('cd /repo/xtr/rm/232460/bot')
pyautogui.press('enter')
pyautogui.typewrite('./antibot-redmine-1.sh 319292')
pyautogui.press('enter')
time.sleep(100)
pyautogui.typewrite('exit')
pyautogui.press('enter')
pyautogui.typewrite('exit')
pyautogui.press('enter')




