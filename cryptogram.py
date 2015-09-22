# create a random letter cypher for a string
import random

def make_dash(string):
    out_string = ''
    for char in string:
        if char != ' ':
            out_string += '-'
        else:
            out_string += char
    return out_string

def make_new_key():
    new_alpha = []
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    alpha_save = alphabet[:]
    while alphabet:
        pick = random.choice(alphabet)
        new_alpha.append(pick)
        index = alphabet.index(pick)
        alphabet.pop(index)
    return dict(zip(alpha_save, new_alpha))

def scramble(string, mapper):
    out_string = ''
    for char in string:
        if char != ' ':
            out_string += mapper[char]
        else:
            out_string += char
    return out_string

sentence = "the quick brown fox jumps over the lazy dog"
new_key = make_new_key()
print(make_dash(sentence))
print(scramble(sentence, new_key))
