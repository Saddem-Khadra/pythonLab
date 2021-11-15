import os

import colorama
from colorama import Fore

from utils import read_csv_file, convert_to_num, write_csv_file


class Fruit:
    def __init__(self, **kwargs):
        self._name = kwargs.get("name")
        self._scores = kwargs.get("scores")
        self._total = sum(self._scores[1:])
        self._result = self._scores[0] * self._total

    def __str__(self, option=None):
        if option:
            return Fore.MAGENTA + f"{self._name} {self._total} {self._result}"
        else:
            return Fore.LIGHTMAGENTA_EX + f"{self._name}: {self._result}"

    def get_name(self):
        return self._name

    def get_total(self):
        return self._total

    def get_result(self):
        return self._result


if __name__ == '__main__':
    colorama.init(autoreset=True)
    my_list = []
    rows = read_csv_file("produce.csv")
    for row in rows:
        row = row[0].split()
        fruit_name = row.pop(0)
        scores = convert_to_num(row)
        fruit = Fruit(name=fruit_name, scores=scores)
        data = [fruit.get_name(), fruit.get_total(), fruit.get_result()]
        my_list.append(data)
        print(fruit.__str__())
    if not os.path.exists("produce.out"):
        write_csv_file("produce.out", data=my_list)
    rows = read_csv_file("produce.csv")
    for row in rows:
        row = row[0].split()
        fruit_name = row.pop(0)
        scores = convert_to_num(row)
        fruit = Fruit(name=fruit_name, scores=scores)
        print(fruit.__str__(option=True))
