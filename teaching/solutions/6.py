# Return the length of the longest word in the provided sentence.
# Your response should be a number.


def find_longest_word_in(string):
    longest = 0
    word_list = string.split(' ')
    for word in word_list:
        if len(word) > longest:
            longest = len(word)
    return longest

print(find_longest_word_in("The quick brown fox jumped over the lazy dog"))

