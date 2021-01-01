def within_range(array, x, k):

    # Using list comprehension, we iterate through the input array,
    # identify elements that are bigger or equal to (x-k),
    # and are also smaller or equal to (x+k), and therefore within the specified range
    # and return a new list containing those elements
    return [i for i in array if (i <= x+k) and (i >= x-k)]


print(within_range([1, 3, 5, 7, 2, 0, 6], 5, 2))