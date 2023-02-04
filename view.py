def get_op():
    op = int(input("Выберите операцию: \n\
            1. Добавление ученика;\n\
            2. Добавление предмета;\n\
            3. Добавить оценку;\n\
            4. Показать список учеников;\n\
            5. Показать лист оценок конкретного ученика;\n\
            6. Выход из программы.\n"))
    return op


def input_student():
    name = input("Введите имя и фамилию: ")
    return name

def input_lesson():
    less = input("Введите предмет: ")
    return less

def input_mark():
    name = input("Введите имя ученика: ")
    less = input("Введите предмет: ")
    mark = input("Введите оценку: ")
    return name,less,mark

def get_name_to_show():
    name = input("Введите имя ученика для просмотра оценок: ")
    return name
