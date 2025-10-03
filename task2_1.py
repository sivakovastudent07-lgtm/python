def flatten_list(lst):
    i = 0
    while i < len(lst):
        if isinstance(lst[i], list):
            flatten_list(lst[i])
            nested = lst.pop(i)
            for j, item in enumerate(nested):
                lst.insert(i + j, item)
        else:
            i += 1
