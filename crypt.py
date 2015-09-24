# simple substitution cypher

numbers = range(1,27)
alphabet = "abcdefghijklmnopqrstuvwxyz"
alpha_dict = dict(zip(alphabet, numbers))
numbers_dict = dict(zip(numbers, alphabet))
# print(alpha_dict, numbers_dict)
def crypt(string, shift):
    output = ''
    for char in string:
        if char.lower() in alphabet:
            offset = alpha_dict[char.lower()] + shift
            if offset > 26:
                offset = offset % 26
            print(offset, numbers_dict[offset])
            output += numbers_dict[offset]
        else:
            output += char
    return output
print(crypt('Zest string!', 5))