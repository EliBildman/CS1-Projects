

# pluralize a word
# in: english word as a string
# out: same word pluralized
def fruit_pluralizer(fruits):
    plural = []
    for fruit in fruits:
        if fruit[-1:] == 'y':
            plural.append(fruit[:-1] + "ies")
        elif fruit[-2:] == 'ch' or fruit[-1:] == "s":
            plural.append(fruit + "es")
        else:
            plural.append(fruit + "s")
    return plural


# reverses a given string
# in: a string of any length
# out: a string of equal length with characters reversed
def my_reverse(forward):
    rev = ""
    for c in forward:
        rev = c + rev
    return rev


def reverse_strings_in_list(list):
    revs = []
    for item in list:
        revs.append(my_reverse(item))
    return revs
