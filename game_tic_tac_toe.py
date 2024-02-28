def print_matrix(my_dict):
    print(my_dict[1], my_dict[2], my_dict[3])
    print(my_dict[4], my_dict[5], my_dict[6])
    print(my_dict[7], my_dict[8], my_dict[9])


def step_pl_1(my_dict):
    k_pl_1 = ""

    while type(k_pl_1) != int or k_pl_1 not in range(1, 10):
        try:
            k_pl_1 = input("Игрок 1: Выберите номер поля (от 1 до 9):")
            k_pl_1 = int(k_pl_1)
            if k_pl_1 not in range(1, 10):
                print("Номер поля указан не корректно. ")
            elif k_pl_1 in range(1, 10):
                break
        except ValueError:
            print("Используйте для ввода только цифры от 1 до 9!")

    if my_dict[k_pl_1] == "[ ]":
        my_dict[k_pl_1] = "[X]"
    else:
        while my_dict[k_pl_1] != "[ ]":
            print("Ячейка занята. Выберите другую.")
            while type(k_pl_1) != int or k_pl_1 not in range(1, 10) or my_dict[k_pl_1] != "[ ]":
                try:
                    k_pl_1 = input(
                        "Игрок 1: Выберите номер поля (от 1 до 9):")
                    k_pl_1 = int(k_pl_1)
                    if k_pl_1 not in range(1, 10):
                        print("Номер поля указан не корректно. ")
                    elif k_pl_1 in range(1, 10):
                        break
                except ValueError:
                    print("Используйте для ввода только цифры от 1 до 9!")
        my_dict[k_pl_1] = "[X]"
    return print_matrix(my_dict)


def step_pl_2(my_dict):
    k_pl_2 = ""

    while type(k_pl_2) != int or k_pl_2 not in range(1, 10):
        try:
            k_pl_2 = input("Игрок 2: Выберите номер поля (от 1 до 9):")
            k_pl_2 = int(k_pl_2)
            if k_pl_2 not in range(1, 10):
                print("Номер поля указан не корректно. ")
            elif k_pl_2 in range(1, 10):
                break
        except ValueError:
            print("Используйте для ввода только цифры от 1 до 9!")

    if my_dict[k_pl_2] == "[ ]":
        my_dict[k_pl_2] = "[0]"
    else:
        while my_dict[k_pl_2] != "[ ]":
            print("Ячейка занята. Выберите другую.")
            while type(k_pl_2) != int or k_pl_2 not in range(1, 10) or my_dict[k_pl_2] != "[ ]":
                try:
                    k_pl_2 = input(
                        "Игрок 2: Выберите номер поля (от 1 до 9):")
                    k_pl_2 = int(k_pl_2)
                    if k_pl_2 not in range(1, 10):
                        print("Номер поля указан не корректно. ")
                    elif k_pl_2 in range(1, 10):
                        break
                except ValueError:
                    print("Используйте для ввода только цифры от 1 до 9!")
    my_dict[k_pl_2] = "[0]"
    return print_matrix(my_dict)


def first_steps(my_dict):
    n = 2
    while n > 0:
        step_pl_1(my_dict)
        step_pl_2(my_dict)
        n -= 1


def win_pl_1(count):
    print("Выиграл игрок №1! ")
    count = 0
    return count


def win_pl_2(count):
    print("Выиграл игрок №2! ")
    count = 0
    return count


def main():
    my_dict = {1: "[ ]", 2: "[ ]", 3: "[ ]", 4: "[ ]",
               5: "[ ]", 6: "[ ]", 7: "[ ]", 8: "[ ]", 9: "[ ]"}
    print_matrix(my_dict)

    first_steps(my_dict)
    count = 5
    while count >= 1:
        step_pl_1(my_dict)
        if count == 5 or count == 3 or count == 1:
            if my_dict[1]+my_dict[2]+my_dict[3] == "[X][X][X]" or my_dict[4]+my_dict[5]+my_dict[6] == "[X][X][X]" or my_dict[7]+my_dict[8]+my_dict[9] == "[X][X][X]":
                win_pl_1(count)
                break
            elif my_dict[1]+my_dict[4]+my_dict[7] == "[X][X][X]" or my_dict[2]+my_dict[5]+my_dict[8] == "[X][X][X]" or my_dict[7]+my_dict[8]+my_dict[9] == "[X][X][X]":
                win_pl_1(count)
                break
            elif my_dict[3]+my_dict[5]+my_dict[7] == "[X][X][X]" or my_dict[1]+my_dict[5]+my_dict[9] == "[X][X][X]":
                win_pl_1(count)
                break
            else:
                count = count - 1
                if count != 0:
                    step_pl_2(my_dict)
                    if my_dict[1]+my_dict[2]+my_dict[3] == "[0][0][0]" or my_dict[4]+my_dict[5]+my_dict[6] == "[0][0][0]" or my_dict[7]+my_dict[8]+my_dict[9] == "[0][0][0]":
                        win_pl_2(count)
                        break
                    elif my_dict[1]+my_dict[4]+my_dict[7] == "[0][0][0]" or my_dict[2]+my_dict[5]+my_dict[8] == "[0][0][0]" or my_dict[7]+my_dict[8]+my_dict[9] == "[0][0][0]":
                        win_pl_2(count)
                        break
                    elif my_dict[3]+my_dict[5]+my_dict[7] == "[0][0][0]" or my_dict[1]+my_dict[5]+my_dict[9] == "[0][0][0]":
                        win_pl_2(count)
                        break
                    else:
                        count = count - 1
                elif count == 0:
                    print("Ничья! Конец игры!")

main()