# Repeat a given string (first argument) n times (second argument).
# Return an empty string if n is a negative number.

def repeat_a(string, num):
    if num < 0:
        return ""
    return string * num

print(repeat_a("abc", 3))
print(repeat_a("abc", -1))
