from description import description
from rules import rules
from menu import menu
import subprocess


clear = lambda: subprocess.call('cls||clear', shell=True) # функция очистки консоли экрана
clear()


def wrong():
    print("-----------------------------------------")
    print(" Вы ввели некорректный номер пункта меню ")


def menuloop():
    while True:
        mode = menu()
        clear()
        if mode == "1":
            description()
            clear()
        elif mode == "2":
            rules()
            clear()
        elif mode == "3":
            
            clear()
        elif mode == "4":
            break
        else:
            wrong()

menuloop()


