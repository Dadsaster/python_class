# Write a function that returns the factorial
# of the provided integer (num)
# Factorials are often represented with the shorthand notation n!
# For example: 5! = 1 * 2 * 3 * 4 * 5 = 120


def factorialize(num):
    if num == 0:
        return 1
    else:
        return num * (num -1) * (num -2) * factorialize(num-3)
#
# print(factorialize(3))
