# Truncate a string (first argument) if it is longer than the given
# maximum string length (second argument). Return the truncated string
# with a "..." ending.
def truncate(string, num):
    if len(string) > num:
        return string[:num-3] + '...'
    return string

print(truncate("A-tisket a-tasket A green and yellow basket", 11))
# should return "A-tisket..."
