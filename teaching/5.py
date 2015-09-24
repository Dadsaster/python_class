# Return true if the given string is a palindrome. Otherwise, return false.
# A palindrome is a word or sentence that's spelled the same way both
# forward and backward, ignoring punctuation, case, and spacing.
# You'll need to remove punctuation and turn everything lower case in order
# to check for palindromes.
# We'll pass strings with varying formats, such as "racecar", "RaceCar",
# and "race CAR" among others.

def palindrome(string):
# make string lower case
# loop through string
    new_string = ''
    for char in string.lower():
        if char in 'abcdefghijklmnopqrstuvwxyz':
            new_string = new_string + char
    print(new_string)
# test if character is in [a-z] - keep
# reverse new string
# compare to forward string

    # return True


# print(palindrome("eye")) # True
print(palindrome("A man, a plan, a canal. Panama")) # True
# print(palindrome("one")) # False