import pyautogui as pag
import keyboard as key
from time import sleep

end_button = input('Enter the shutdown button (only Latin letters): ')

sleep(3.5)

while True:
	pag.tripleClick()
	if key.is_pressed(end_button):
		break
