import string

import colorama
from colorama import Fore

from utils import read_file

if __name__ == '__main__':
    letters = list(string.ascii_lowercase)
    colorama.init(autoreset=True)
    lines = read_file('exemple.txt')
    for letter in letters:
        count = 0
        for line in lines:
            count += line.lower().count(letter)
        print(Fore.LIGHTMAGENTA_EX + f"{letter} => {count}")
