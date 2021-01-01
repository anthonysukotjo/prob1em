def within_range(array, x, k):

    # Using list comprehension, we iterate through the input array
    # and return a new list that meets the conditions ( is within the specified range)
    return [i for i in array if (i <= x+k) and (i >= x-k)]


print(within_range([1, 3, 5, 7, 2, 0, 6], 5, 2))