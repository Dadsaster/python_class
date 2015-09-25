import pprint

pp = pprint.PrettyPrinter(indent=4)

def get_text(filename):
    f = open(filename, 'r')
    text = f.read()
    f.close()
    return text

def count_words(words):
    counter = {}
    word_list = words.split()
    for word in word_list:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    pp.pprint(counter)


words = get_text('alice.txt')
count_words(words)
