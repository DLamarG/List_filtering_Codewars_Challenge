def filter_list(l):
    filtered_list = list([x for x in l if isinstance(x, int)])
    return(filtered_list)
print(filter_list([1, 2, 6, '456', 2, '43']))
print(filter_list([1, 2, 467, '456', 2, '0']))
print(filter_list([1, -456, 456, '456', 2, '43']))
print(filter_list(['56', 2, 456, '987897', 2, '43']))
print(filter_list(['8', 2, '456', 676, 2, '43']))