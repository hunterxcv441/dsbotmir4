import sqlite3
import time
import pyfiglet
import pr1

linha = '-' * 77
print("\n" * 10)
ascii_banner = pyfiglet.figlet_format("BUCH BOT")
print(ascii_banner)
inicio = input('Iniciar Programa(S/N): ')


def menu():
    try:
        if (inicio == 'S' or 's'):
            tokenS = input('TOKEN >: ')#OTEyMDE3NDUwMzkwOTM3Njkw.YZp0cA.vZiQbDO8hbkG-FWmPstHrLkksO4
            pr1.botpr1(tokenS)
    except:
        menu()

menu()