import colorama
from colorama import Fore

from utils import add_to_file, show_details_of_students, show_top_students


class Student:
    def __init__(self, **kwargs):
        self._name = kwargs.get("name")
        self._exam_scores = kwargs.get("exam_scores")

    def __setattr__(self, key, value):
        if key == "_name" and not (isinstance(value, str) and value.isalpha()):
            raise TypeError(f'{value} must be an string')
        elif key == "_exam_scores" and not (isinstance(value, list) and self.check_int_float(value)):
            raise TypeError(f'{value} must be an list of numbers')
        super(Student, self).__setattr__(key, value)

    def __str__(self):
        return Fore.MAGENTA + f"{self._name}"

    def check_int_float(self, my_list):
        return all(isinstance(i, (int, float)) for i in my_list)

    def add_student_to_file(self):
        file = open("studentdata.txt", "a")
        file.write(f"{self._name} {' '.join(str(item) for item in self._exam_scores)}" + "\n")
        file.close()

    def student_exam_scores_details(self):
        print(Fore.CYAN + "Average : " + Fore.MAGENTA + str(sum(self._exam_scores) / len(self._exam_scores)))
        print(Fore.CYAN + "Min : " + Fore.MAGENTA + str(min(self._exam_scores)))
        print(Fore.CYAN + "Max : " + Fore.MAGENTA + str(max(self._exam_scores)))


if __name__ == '__main__':
    colorama.init(autoreset=True)
    choice = 0
    print(Fore.LIGHTCYAN_EX + "### Welcome To UIT !! ###")
    while True:
        print(Fore.YELLOW + "which action do you want to make ?")
        print(Fore.CYAN + "1. add student")
        print(Fore.CYAN + "2. show students that have more than six exam scores")
        print(Fore.CYAN + "3. show details of students")
        try:
            choice = int(input())
            if choice == 1:
                add_to_file(Student)
            elif choice == 2:
                show_top_students(Student)
            elif choice == 3:
                show_details_of_students(Student)
            else:
                print(Fore.RED + f"{choice} Not a Choice from above!")
                continue
        except ValueError as e:
            print(Fore.RED + f"{e.__str__()}")
            continue
        else:
            break
