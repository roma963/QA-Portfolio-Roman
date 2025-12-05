import json
import os

DATA_FILE = "diary.json"

def load_data():
    """Загружает данные из файла."""
    if not os.path.exists(DATA_FILE):
        return {}, {}

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data.get("students", {}), data.get("students_marks", {})


def save_data(students, students_marks):
    """Сохраняет данные в JSON файл."""
    data = {
        "students": students,
        "students_marks": students_marks
    }
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

students, students_marks = load_data()
   
def print_all_marks():
    for student, marks in students_marks.items():
        print(f"\n{student}:")
        for subject, grades in marks.items():
            print(f"  {subject} - {grades}")
    print()


def add_student():
    name = input("Введите имя нового ученика: ")
    if name in students:
        print("Такой ученик уже существует.\n")
        return

    students[name] = True
    students_marks[name] = {}
    print(f"Ученик {name} добавлен\n")
    save_data(students, students_marks)


def delete_student():
    name = input("Введите имя ученика для удаления: ")
    if name not in students:
        print("Такого ученика нет.\n")
        return

    students.pop(name)
    students_marks.pop(name)
    print(f"Ученик {name} удалён\n")
    save_data(students, students_marks)


def add_subject():
    subject = input("Введите название нового предмета: ")

    for student in students:
        students_marks[student].setdefault(subject, [])

    print(f"Предмет {subject} добавлен\n")
    save_data(students, students_marks)


def delete_subject():
    subject = input("Введите название предмета для удаления: ")

    for student in students:
        students_marks[student].pop(subject, None)

    print(f"Предмет {subject} удалён\n")
    save_data(students, students_marks)


def add_mark():
    student = input("Введите имя ученика: ")
    if student not in students:
        print("Ученика нет.\n")
        return

    subject = input("Введите предмет: ")
    if subject not in students_marks[student]:
        print("Предмета нет.\n")
        return

    mark = int(input("Введите оценку: "))
    students_marks[student][subject].append(mark)
    print("Оценка добавлена\n")
    save_data(students, students_marks)


def show_student_marks():
    name = input("Введите имя ученика: ")
    if name not in students:
        print("Ученика нет.\n")
        return

    print(f"\nОценки {name}:")
    for subject, marks in students_marks[name].items():
        print(f"{subject}: {marks}")
    print()

print("ТЕКУЩИЕ ДАННЫЕ:")
print_all_marks()

while True:
    print("""
Список команд:
1. Добавить оценку ученика по предмету
2. Показать оценки одного ученика
3. Добавить нового ученика
4. Удалить ученика
5. Добавить новый предмет
6. Удалить предмет
7. Выход из программы
""")

    cmd = input("Введите номер команды: ")

    if cmd == "1":
        add_mark()
    elif cmd == "2":
        show_student_marks()
    elif cmd == "3":
        add_student()
    elif cmd == "4":
        delete_student()
    elif cmd == "5":
        add_subject()
    elif cmd == "6":
        delete_subject()
    elif cmd == "7":
        print("Данные сохранены. Выход.")
        break
    else:
        print("Неизвестная команда.\n")
