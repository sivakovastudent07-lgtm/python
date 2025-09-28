def unique_elements(list):
    result = []  

    def flatten(lst):
        for i in lst:
            if type(i) == list:  
                flatten(i)  
            else:
                if i not in result:
                    result.append(i)  

    flatten(list)
    return result
