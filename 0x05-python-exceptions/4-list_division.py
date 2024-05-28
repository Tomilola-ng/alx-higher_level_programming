#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    final = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                final.append(0)
            else:
                a = my_list_1[i]
                b = my_list_2[i]
                if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                    print("wrong type")
                    final.append(0)
                else:
                    final.append(a / b)
        except ZeroDivisionError:
            print("division by 0")
            final.append(0)
        except Exception:
            final.append(0)
    return final
