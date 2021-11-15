import colorama
from colorama import Fore

from utils import read_file

if __name__ == '__main__':
    colorama.init(autoreset=True)
    lines = read_file('a.txt')
    print(Fore.LIGHTMAGENTA_EX+f"we have {len(lines)} name in the file")
