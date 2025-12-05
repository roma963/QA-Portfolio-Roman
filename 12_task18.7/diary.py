import random

students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()

classes = ['Математика', 'Русский язык', 'Информатика']

students_marks = {}

for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1, 5) for _ in range(3)]
        students_marks[student][class_] = marks

def print_menu():
    print('''
Список команд:
 1. Добавить оценку ученика по предмету
 2. Вывести средний балл по всем предметам по каждому ученику
 3. Вывести все оценки по всем ученикам
 4. Удалить оценку ученика по предмету
 5. Изменить (отредактировать) оценку ученика по предмету
 6. Добавить нового ученика
 7. Удалить ученика
 8. Добавить новый предмет
 9. Удалить предмет
10. Показать все оценки одного ученика
11. Показать средний балл по всем предметам для одного ученика
 0. Выход из программы
''')

def get_student():
    """Запрос имени ученика и проверка существования."""
    student = input('Введите имя ученика: ')
    if student not in students_marks:
        print('ОШИБКА: такого ученика нет.')
        return None
    return student

def get_subject(student):
    """Запрос предмета и проверка существования для конкретного ученика."""
    class_ = input('Введите предмет: ')
    if class_ not in students_marks[student]:
        print('ОШИБКА: такого предмета нет.')
        return None
    return class_

def show_all_marks():
    """Вывод всех оценок по всем ученикам."""
    for student in students:
        print(student)
        for class_ in classes:
            marks = students_marks[student].get(class_, [])
            print(f'\t{class_} - {marks}')
        print()

def show_avg_all():
    """Средний балл по всем предметам по каждому ученику."""
    for student in students:
        print(student)
        for class_ in classes:
            marks = students_marks[student].get(class_, [])
            if marks:
                avg = sum(marks) / len(marks)
                print(f'{class_} - {avg:.2f}')
            else:
                print(f'{class_} - нет оценок')
        print()

def show_student_marks(student):
    """Все оценки конкретного ученика."""
    print(f'Оценки ученика: {student}')
    for class_ in classes:
        marks = students_marks[student].get(class_, [])
        print(f'\t{class_} - {marks}')
    print()

def show_student_avg(student):
    """Средний балл по всем предметам одного ученика."""
    print(f'Средний балл ученика: {student}')
    for class_ in classes:
        marks = students_marks[student].get(class_, [])
        if marks:
            avg = sum(marks) / len(marks)
            print(f'{class_} - {avg:.2f}')
        else:
            print(f'{class_} - нет оценок')
    print()

print_menu()

while True:
    try:
        command = int(input('Введите номер команды: '))
    except ValueError:
        print('Нужно ввести число команды.')
        continue

    if command == 0:
        print('Выход из программы.')
        break

    elif command == 1:
        print('1. Добавить оценку ученика по предмету')
        student = get_student()
        if not student:
            continue
        class_ = get_subject(student)
        if not class_:
            continue
        try:
            mark = int(input('Введите оценку (1–5): '))
        except ValueError:
            print('ОШИБКА: нужно ввести число.')
            continue
        students_marks[student][class_].append(mark)
        print(f'Для {student} по предмету {class_} добавлена оценка {mark}')

    elif command == 2:
        print('2. Средний балл по всем предметам по каждому ученику')
        show_avg_all()

    elif command == 3:
        print('3. Все оценки по всем ученикам')
        show_all_marks()

    elif command == 4:
        print('4. Удалить оценку ученика по предмету')
        student = get_student()
        if not student:
            continue
        class_ = get_subject(student)
        if not class_:
            continue
        marks = students_marks[student][class_]
        if not marks:
            print('У этого ученика по этому предмету пока нет оценок.')
            continue
        print('Текущие оценки:', list(enumerate(marks, start=1)))
        try:
            idx = int(input('Номер оценки для удаления: ')) - 1
            if idx < 0 or idx >= len(marks):
                print('ОШИБКА: нет оценки с таким номером.')
                continue
            deleted = marks.pop(idx)
            print(f'Оценка {deleted} удалена.')
        except ValueError:
            print('ОШИБКА: нужно ввести число.')

    elif command == 5:
        print('5. Изменить (отредактировать) оценку ученика по предмету')
        student = get_student()
        if not student:
            continue
        class_ = get_subject(student)
        if not class_:
            continue
        marks = students_marks[student][class_]
        if not marks:
            print('У этого ученика по этому предмету пока нет оценок.')
            continue
        print('Текущие оценки:', list(enumerate(marks, start=1)))
        try:
            idx = int(input('Номер оценки для изменения: ')) - 1
            if idx < 0 or idx >= len(marks):
                print('ОШИБКА: нет оценки с таким номером.')
                continue
            new_mark = int(input('Новое значение оценки (1–5): '))
            old_mark = marks[idx]
            marks[idx] = new_mark
            print(f'Оценка {old_mark} изменена на {new_mark}.')
        except ValueError:
            print('ОШИБКА: нужно ввести число.')

    elif command == 6:
        print('6. Добавить нового ученика')
        new_student = input('Введите имя нового ученика: ')
        if new_student in students_marks:
            print('Такой ученик уже есть.')
        else:
            students.append(new_student)
            students.sort()
            students_marks[new_student] = {}
            for class_ in classes:
                students_marks[new_student][class_] = []
            print(f'Ученик {new_student} добавлен.')

    elif command == 7:
        print('7. Удалить ученика')
        student = get_student()
        if not student:
            continue
        students.remove(student)
        del students_marks[student]
        print(f'Ученик {student} удалён из дневника.')

    elif command == 8:
        print('8. Добавить новый предмет')
        new_class = input('Введите название нового предмета: ')
        if new_class in classes:
            print('Такой предмет уже есть.')
        else:
            classes.append(new_class)
            for student in students:
                students_marks[student][new_class] = []
            print(f'Предмет {new_class} добавлен.')

    elif command == 9:
        print('9. Удалить предмет')
        class_ = input('Введите название предмета для удаления: ')
        if class_ not in classes:
            print('Такого предмета нет.')
        else:
            classes.remove(class_)
            for student in students:
                students_marks[student].pop(class_, None)
            print(f'Предмет {class_} удалён.')

    elif command == 10:
        print('10. Показать все оценки одного ученика')
        student = get_student()
        if student:
            show_student_marks(student)

    elif command == 11:
        print('11. Показать средний балл по всем предметам для одного ученика')
        student = get_student()
        if student:
            show_student_avg(student)

    else:
        print('Неизвестная команда, попробуйте ещё раз.')

