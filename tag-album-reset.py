import eyed3
import os
from colorama import Fore, Back, Style

dir_path = os.path.dirname(os.path.realpath(__file__))

def imprimir(text):
    print(Fore.BLACK + Back.WHITE + text + Style.RESET_ALL)

for file in os.listdir(dir_path):
    if file[-3:] == 'mp3':
        imprimir(file)
        print()

        try:
            song = eyed3.load(file)
            song.tag.album = ""
            song.tag.save()
        except Exception as e:
            print(Fore.WHITE + Back.RED + file + " - " + str(e) + Style.RESET_ALL + "\n")