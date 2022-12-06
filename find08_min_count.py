def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    i = 0
    n = data[0]
    while i < len(data):
        if n > data[i]:
            n = data[i]
        i += 1
    return data.count(n)
print(find_min_count([0, -4, 3, 9, -2, -4]))
