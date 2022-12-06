def find_min_index(data):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    i = 0
    n = data[0]
    while i < len(data):
        if n > data[i]:
            n = data[i]
        i += 1
    return data.index(n)
print(find_min_index([12, 2, 5, 2, 7, 9, 1]))
    

