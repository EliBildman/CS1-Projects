def count_vowels(a_string):
    vowels = ["a" ,"e", "i", "o", "u"]
    num_vowels = 0
    for x in a_string:
        if x.lower() in vowels:
            num_vowels += 1
    return num_vowels


def de_vowel(a_string):
    vowels = ["a", "e", "i", "o", "u"]
    i = 0
    while i < len(a_string):
        if a_string[i] in vowels:
            a_string = a_string[:i] + a_string[i+1:]
        i += 1
    return a_string


print(de_vowel("Hello world"))
