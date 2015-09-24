# You will be provided with an initial list (the first argument
# in the destroyer function), followed by one or more arguments.
# Remove all elements from the initial array that are of the same
# value as these arguments.

def destroyer(first, *argv):
    for item in argv:
        while item in first:
            first.remove(item)
    return first

print(destroyer([1, 2, 3, 1, 2, 3], 2, 3))
# should return [1, 1]
