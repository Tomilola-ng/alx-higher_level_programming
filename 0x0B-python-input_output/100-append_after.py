#!/usr/bin/python3
""" SEARCH AND UPDATE """


def append_after(filename="", search_string="", new_string=""):
    """ We first open then search then append """

    read_text = ""

    with open(filename) as my_file:
        read_text = my_file.readlines()

    with open(filename, mode="w") as write_file:
        new_str = ""

        for line_txt in read_text:
            new_str += line_txt
            if search_string in line_txt
            new_str += search_string

        write_file.write(new_str)
