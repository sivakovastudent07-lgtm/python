def merge_dicts(dict1, dict2):
    for key in dict2:
        if key in dict1:
            if type(dict1[key]) == dict and type(dict2[key]) == dict:
                merge_dicts(dict1[key], dict2[key])
            else:
                dict1[key] = dict2[key] 
        else:
            dict1[key] = dict2[key]
