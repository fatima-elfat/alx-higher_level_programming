#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_l = []
    for i in range(list_length):
        r = 0
        try:
            r = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except (ValueError, ZeroDivisionError):
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            my_l.append(r)
    return my_l
