# Return the remaining elements of an array after chopping off n elements from the head.
def slasher(array, chop):
    return array[chop:]


print(slasher([1, 2, 3], 2))
# should return [3]
