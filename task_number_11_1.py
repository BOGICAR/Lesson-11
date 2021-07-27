# Задание №1 - сделано
def u_input():
    list_1 = []
    user_input = 1
    while user_input != '':
        user_input = input()
        list_1.append(user_input)
    return list_1


def task_11_1():
    us_input = u_input()
    with open('task_11_1.txt', 'w') as file:
        for i in us_input:
            file.write(i+'\n')


task_11_1()
