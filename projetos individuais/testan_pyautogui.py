import pyautogui as py
import time

py.press('win')
py.write('chrome')
py.press('enter')
time.sleep(1.3)
py.click(x=289, y=634)

time.sleep(1)
py.click(x=427, y=63)
py.write('https://sigpas.seplag.mt.gov.br/sigpas/')
py.press('enter')

time.sleep(3.5)
py.click(x=453, y=369)
py.write('358726')
py.click(x=452, y=423)
py.write('Pedro@273')
py.click(x=349, y=513)

time.sleep(5)
py.click(x=459, y=596)
