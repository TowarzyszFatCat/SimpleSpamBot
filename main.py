import pyautogui as pag
from time import sleep

with open("plik.txt", "r", encoding="utf-8") as f:
    odczytany = f.readlines()
    print(odczytany)

sleep(2)

for line in odczytany:
    print(line)
    sleep(0.5)   # Czas pomiędzy wiadomościami
    pag.typewrite(line)
    pag.press('Enter')
