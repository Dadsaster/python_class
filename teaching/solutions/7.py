# Check if a string (first argument) ends with
# the given target string (second argument).

def confirm_end_of(string, target):
    return string[-len(target):] == target

print(confirm_end_of("Bastian", "n"))
print(confirm_end_of("Connor", "n"))
print(confirm_end_of("He has to give me a new name", "name"))
