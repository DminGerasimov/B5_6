from description import description
from rules import rules
from menu import menu
import subprocess


clear = lambda: subprocess.call('cls||clear', shell=True) # функция очистки консоли экрана
clear()
L = [] # игровое поле


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
    print("")


def ask_step(v_h_str, x_o):                     # ввод игроком позиции на игровом поле
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


def ask_yes_no(info):   # функция заправшивает Yes, No и возвращвет True/False соответственно
    while True:
        yn = input(info)
        if len(yn):
            if yn[0].lower() == "y":
                print(1, yn[0])
                return True
            elif yn[0].lower() == "n":
                print(2, yn[0])
                return False
            else:
                print(" Вы ввели некорректный ответ!")


def swich_current_player(cp):          # переключение текущего игрока "х" <--> "0"
    return "x" if cp == "0" else "0"

def check_winner(L, cp):    # проверка условия обеды игрока
    temp = []               # перевод сложного списка в простой
    for ind in range(1, 4):
        t = L[ind]
        for ind_ in range(1, 4):
            temp.append(t[ind_])

    # проверка вертикальных линий
    for ind in range(0, 3):
        d1 = temp[ind:9:3]
        if d1[0] == cp and d1[1] == cp and d1[2] == cp:
            return True

    # проверка диагоналей
    d1 = temp[0:9:4]
    if d1[0] == cp and d1[1] == cp and d1[2] == cp:
        return True
    d1 = temp[2:9:2]
    if d1[0] == cp and d1[1] == cp and d1[2] == cp:
        return True

    # проверка горизонтальных линий
    for horiz in L:
        if horiz[1] == cp and horiz[2] == cp and horiz[3] == cp:
            return True
    
    return False


def playgame(): # основной игровой цикл программы
    сurrent_player = "x" # текущий игрок
    current_step = 0 # текущий ход
    clear()
    L = construct_matrix()
    prn_matix(L) # Печать чистой матрицы игрового поля
    while True:
        v = ask_step("позиции по вертикали", сurrent_player)
        h = ask_step("позиции по горизонтали", сurrent_player)
        print(v, h)
        temp = L[h]
        if temp[v] != "_": # проверка на изменение позиции игрового поля
            print(f"Данное поле ({v} по вертикали и {h} по горизонтали) уже занято.\nПовторите ход.")
        else:
            current_step += 1 # инкремент текущего хода
            temp[v] = сurrent_player
            L[h] = temp
            clear()
            prn_matix(L)
            if check_winner(L, сurrent_player):
                print(f"\n       Поздравляем!!! Победил игрок {сurrent_player}")
                if ask_yes_no("\n Сыграть ещё раз? (Yes/No): "):
                    L = construct_matrix()
                    сurrent_player = "x"
                    clear()
                    prn_matix(L) # Печать чистой матрицы игрового поля
                    current_step = 0
                    continue
                else:
                    break
            elif current_step == 9 and not check_winner(L, сurrent_player):
                if ask_yes_no("\n Ничья! Сыграть ещё раз? (Yes/No): "):
                    L = construct_matrix()
                    clear()
                    prn_matix(L) # Печать чистой матрицы игрового поля
                    current_step = 0
                    continue
                else:
                    break
            сurrent_player = swich_current_player(сurrent_player)



def wrong():
    print(" _______________________________________ ")
    print(" Вы ввели некорректный номер пункта меню ")
    print(" _______________________________________ ")



def menuloop():             # цикл обработки меню
    while True:
        mode = menu()
        clear()
        if mode == "1":     # описание
            description()
            clear()
        elif mode == "2":   # правила игры
            rules()
            clear()
        elif mode == "3":   # играть
            playgame()
            clear()
        elif mode == "4":   # выход из программы
            break
        else:
            wrong()

menuloop()
