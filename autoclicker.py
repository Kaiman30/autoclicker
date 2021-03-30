import pyautogui as pag
import keyboard as key
from time import sleep

end_button = input('Введите кнопку выключения (только латинские буквы): ')

sleep(3.5)

while True:
	pag.tripleClick()
	if key.is_pressed(end_button):
		break