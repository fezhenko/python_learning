def new_list(q: list):
    new_list = [i for i in q if isinstance(i, int) and i > 0]
    return new_list


def new_list1(q: list):
    new_list1 = [i if isinstance(i, int) else 0 for i in q]
    return new_list1


def new_list2(q: list):
    """Convert items in list to float and then sum the items"""
    new_list2 = sum([float(i) for i in q if isinstance(i, int)])
    return new_list2


my_list = [0, -7, -5, 1, 2, 3, 4, 5, 6, 7, 'qwe']

print(new_list2(my_list))
