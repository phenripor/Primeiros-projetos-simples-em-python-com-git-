import pyautogui 
import time 

pyautogui.PAUSE = 0.8

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2.5)
pyautogui.click(x=828, y=556)
time.sleep(2)
pyautogui.click(x=848, y=640)
time.sleep(15)
pyautogui.click(x=502, y=461)
pyautogui.write("Não fui eu que escrevi isso.")
pyautogui.press('enter')