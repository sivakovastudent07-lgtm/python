def unique_elements(lst):
    """
    возвращает список уникальных элементов из воженного списка,
    сохраняя порядок
    """
    result = []

    def flatten(current_list, output):
        for item in current_list:
            if isinstance(item, list):
                flatten(item, output)
            else:
                if item not in output:
                    output.append(item)

    flatten(lst, result)
    return result