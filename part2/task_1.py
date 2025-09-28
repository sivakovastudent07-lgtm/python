def flatten_list(lst):
    i = 0
    while i < len(lst):
        if type(lst[i]) == list:
            flatten_list(lst[i])  # рекурсия
            nested = lst[i]
            lst.pop(i)
            j = 0
            while j < len(nested):
                lst.insert(i + j, nested[j])
                j += 1
        else:
            i += 1

