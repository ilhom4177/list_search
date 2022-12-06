def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    i = 0
    n = data[0]
    while i < len(data):
        if n < data[i] and data[i] % 2 == 1:
            n = data[0]
        i += 1
    return n
print(find_max_odd([1, 8, 3, 8, 5]))