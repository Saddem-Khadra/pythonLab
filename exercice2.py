import colorama
from colorama import Fore

from utils import read_file, convert_to_num

if __name__ == '__main__':
    colorama.init(autoreset=True)
    lines1 = set(convert_to_num(read_file('num1.txt')))
    lines2 = set(convert_to_num(read_file('num2.txt')))
    result = sorted(lines1.intersection(lines2))
    print(Fore.LIGHTMAGENTA_EX + f"The numbers that are overlapping {result}")
