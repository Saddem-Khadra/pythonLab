import csv

from colorama import Fore


def write_csv_file(file_name, data):
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
        file.close()


def read_csv_file(file_name):
    rows = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows.append(row)
    return rows


def read_file(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    if not len(lines) == 0:
        return lines
    else:
        raise ValueError(f"{file_name} is empty!!")


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


def add_to_file(Student):
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


def show_top_students(Student):
    lines = read_file("files/studentdata.txt")
    print(Fore.LIGHTCYAN_EX + "The students that have more than six exam scores :")
    for line in lines:
        line = line.split()
        if len(line) >= 6:
            student_name = line.pop(0)
            print(Student(name=student_name, exam_scores=convert_to_num(line)))


def show_details_of_students(Student):
    lines = read_file("files/studentdata.txt")
    print(lines)
    print(Fore.LIGHTCYAN_EX + "List of details of each student : ")
    for line in lines:
        line = line.split()
        student_name = line.pop(0)
        student = Student(name=student_name, exam_scores=convert_to_num(line))
        print(Fore.LIGHTMAGENTA_EX + "###############")
        print(f"Student : {student}")
        student.student_exam_scores_details()
