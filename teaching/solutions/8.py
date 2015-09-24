# Write a function that splits a list (first argument)
# into groups the length of size (second argument)
# and returns them as a multidimensional array.

def chunk(array, size):
    new_list = []
    while len(array):
        new_list.append(array[:size])
        array[:size] = []
    return new_list


print(chunk([0, 1, 2, 3, 4, 5], 3))
# should return [[0, 1, 2], [3, 4, 5]]
print(chunk(["a", "b", "c", "d"], 2))
# should return [["a", "b"], ["c", "d"]]
