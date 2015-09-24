# Return the length of the longest word in the provided sentence.
# Your response should be a number.


def find_longest_word_in(string):
    longest = 0
    # turn string into list
    list = string.split()
    # loop through list
    for word in list:
    # check length of each against variable 'longest'
        if len(word) > longest:
            longest = len(word)
    # if length of word is > 'longest' - make it the longest
    # at end of looping return longest

    return longest

print(find_longest_word_in("The quick brown fox jumped over the lazy dog"))
# should return 6