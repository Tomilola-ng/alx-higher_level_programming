#!/usr/bin/python3
def search_replace(my_list, search, replace):
  my_new_list = []
  for item in my_list:
    if item == search:
      my_new_list.append(replace)
    else:
        my_new_list.append(item)
  return my_new_list
