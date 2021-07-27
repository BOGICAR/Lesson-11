# Задание №3 - сделано
def task_11_3(list_, shift_distance):
    if shift_distance < 0:
        shift_distance = abs(shift_distance)
        for i in range(shift_distance):
            list_.append(list_.pop(0))
    else:
        for i in range(shift_distance):
            list_.insert(0, list_.pop())
    return list_


list_11_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(task_11_3(list_11_3, -4))
