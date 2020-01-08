#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for x in range(0, list_length):
        try:
            new_list.append(my_list_1[x] / my_list_2[x])
        except (TypeError, ValueError):
            print("wrong type")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        finally:
            pass
    return new_list
