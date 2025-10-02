def merge_sorted_list(l1, l2):  
    merged = []
    i, j = 0, 0

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1

    while i < len(l1):
        merged.append(l1[i])
        i += 1
    while j < len(l2):
        merged.append(l2[j])
        j += 1

    return merged