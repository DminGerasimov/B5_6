from description import description
from rules import rules
from managment import managment
from menu import menu
import subprocess


clear = lambda: subprocess.call('cls||clear', shell=True)
clear()
description()
rules()
managment()
menu()