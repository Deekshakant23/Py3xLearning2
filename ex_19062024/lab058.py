# how to use list in user define function

numbers = [10, 20, 20, 30]


def list_function(deeksha_list):
    deeksha_list.append(60)
    deeksha_list[1] = 80
    return deeksha_list


result = list_function(deeksha_list=numbers)
print(result)
