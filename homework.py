l_1 = [1,11,14,5,8,9]

def exc1 (list):
    placeholder_list = []
    for num in list:
        if num < 10:
            placeholder_list.append(num)
    return placeholder_list

print(exc1(l_1))

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def exc2 (list1, list2):
    return sorted(list1 + list2)

print(exc2(l_1, l_2))