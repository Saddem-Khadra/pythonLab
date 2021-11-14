import colorama
from colorama import Fore


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


def read_file(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    if not len(lines) == 0:
        return lines
    else:
        raise ValueError(f"{file_name} is empty!!")


def show_details_of_students():
    lines = read_file("studentdata.txt")
    print(lines)
    print(Fore.LIGHTCYAN_EX + "List of details of each student : ")
    for line in lines:
        line = line.split()
        student_name = line.pop(0)
        student = Student(name=student_name, exam_scores=convert_to_num(line))
        print(Fore.LIGHTMAGENTA_EX + "###############")
        print(f"Student : {student}")
        student.student_exam_scores_details()


def show_top_students():
    lines = read_file("studentdata.txt")
    print(Fore.LIGHTCYAN_EX + "The students that have more than six exam scores :")
    for line in lines:
        line = line.split()
        if len(line) >= 6:
            student_name = line.pop(0)
            print(Student(name=student_name, exam_scores=convert_to_num(line)))


def convert_to_num(my_list):
    new_list = []
    for i in my_list:
        if "." in i:
            try:
                new_list.append(float(i))
            except:
                raise TypeError(f'{i} must be a number')
        else:
            try:
                new_list.append(int(i))
            except:
                raise TypeError(f'{i} must be a number')
    return new_list


def add_to_file():
    number_of_students = 0
    while True:
        print(Fore.YELLOW + "How many students you want to add to the class ??")
        try:
            number_of_students = int(input())
        except ValueError as e:
            print(Fore.RED + f"{e.__str__()} Not an Integer !")
            continue
        else:
            break
    print(Fore.CYAN + "Enter the name and the exam scores of the student")
    print(Fore.LIGHTWHITE_EX + "Please follow this exemple :")
    print(Fore.LIGHTBLUE_EX + "Saddem 20 20 20 20 20 20 20 20")

    for number in range(1, number_of_students + 1):
        while True:
            try:
                res = input(Fore.GREEN + f"Student N°{number} : ").split()
                name = res.pop(0)
                exam_scores = convert_to_num(res)
                student = Student(name=name, exam_scores=exam_scores)
                student.add_student_to_file()
                print(f"{student} has been added successfully!")
            except TypeError as e:
                print(Fore.RED + e.__str__())
                continue
            else:
                break


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
                add_to_file()
            elif choice == 2:
                show_top_students()
            elif choice == 3:
                show_details_of_students()
            else:
                print(Fore.RED + f"{choice} Not a Choice from above!")
                continue
        except ValueError as e:
            print(Fore.RED + f"{e.__str__()}")
            continue
        else:
            break
