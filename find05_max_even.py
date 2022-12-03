def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    i=0 
    max1=data[0]
    while i<len(data):
        if max1<data[i] and data[i]%2==0:
            max1=data[i]
        i+=1
    return max1 
print(find_max_even([1,2,3,4,5,6,7]))
