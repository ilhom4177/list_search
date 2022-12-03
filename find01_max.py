def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    i=0 
    max1=data[0]
    while i<len(data):
        if max1<data[i]:
            max1=data[i]
        i+=1
    return max1 
    
print(find_max([1,2,3,4,5,6]))
    