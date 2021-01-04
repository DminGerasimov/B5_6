from description import description
from rules import rules
from menu import menu
import subprocess


clear = lambda: subprocess.call('cls||clear', shell=True) # функция очистки консоли экрана
clear()
L = [] # игровое поле

def wrong():
    print(" _______________________________________ ")
    print(" Вы ввели некорректный номер пункта меню ")
    print(" _______________________________________ ")


def construct_matrix():  # инициализация матрицы [4x4] игрового поля
    L = [[" ", "1", "2", "3"], ["1", "_", "_", "_"], ["2", "_", "_", "_"], ["3", "_", "_", "_"]]
    return L


def prn_matix(L):                   # печать текущего состояния игрового поля
    print("\n    Игровое поле\n")
    for h in range(len(L)):
        text = ""
        temp = L[h]
        for v in range (len(temp)):
            text += " " + str(temp[v])
        print("   " + text)


def ask_step(v_h_str, x_o):                     # ввод позиции на игровом поле
    number = None
    while number is None:
        num_str =  input(f"  Игрок {x_o}, ведите номер {v_h_str} от 1 до 3: ")
        if num_str.isdigit():
            number = int(num_str)
            if 1 <= number <= 3:                # проверка диапазона введенного числа
                return number
            print(" Вы ввели некорректное число!")
            number = None
            continue
        else:
            print(" Вы ввели некорректное число!")
            continue


def swich_current_player(cp):                     # переключение текущего игрока "х" <--> "0"
    return "x" if cp == "0" else "0"


def playgame(): # игровой цикл
    сurrent_player = "x"
    clear()
    prn_matix(construct_matrix()) # Печать чистой матрицы игрового поля
    while True:
        print(str(ask_step("позиции по вертикали", сurrent_player)))
        print(str(ask_step("позиции по горизонтали", сurrent_player)))
        сurrent_player = swich_current_player(сurrent_player)
        input("\nНажмите Enter для продолжения")


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
            playgame()
            clear()
        elif mode == "4":
            break
        else:
            wrong()

menuloop()
