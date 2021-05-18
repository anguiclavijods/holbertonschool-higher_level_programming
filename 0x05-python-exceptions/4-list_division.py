#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_result = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            print("{}".format(result))
        except TypeError:
            result = 0
            print("wrong type")
        except IndexError:
            print("out of range")
            result = 0
        except ZeroDivisionError:
            value = 0
            print("division by 0")
        finally:
            new_result.append(result)
    return new_result