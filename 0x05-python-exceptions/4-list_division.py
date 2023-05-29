#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    size = list_length

    for index in range(0, size):
        try:
            first = my_list_1[index]
            second = my_list_2[index]
            new_list.append(first / second)
        except IndexError:
            print("out of range")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except (ValueError, TypeError):
            print("wrong type")
            new_list.append(0)
        finally:
            pass
    return new_list
