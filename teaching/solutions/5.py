# Return true if the given string is a palindrome. Otherwise, return false.
# A palindrome is a word or sentence that's spelled the same way both
# forward and backward, ignoring punctuation, case, and spacing.
# You'll need to remove punctuation and turn everything lower case in order
# to check for palindromes.
# We'll pass strings with varying formats, such as "racecar", "RaceCar",
# and "race CAR" among others.

def palindrome(string):
    output = ''
    for char in string:
        if char.lower() in 'abcdefghijklmnopqrstuvwxyz':
            output = output + char.lower()
    return output == output[::-1]

print(palindrome("eye"))
print(palindrome("A man, a plan, a canal. Panama"))
print(palindrome("one"))