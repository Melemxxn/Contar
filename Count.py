import keyboard
from pyautogui import write

numero = int(input("Introduce el numero: "))

while True:
    keyboard.wait("enter")
    numero = numero + 2
    write(str(numero))