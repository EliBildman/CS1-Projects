def get_freq(paragraph):
    paragraph_lower = paragraph.lower()
    paragraph_lower_no_punctuation = paragraph_lower.replace(".", "")
    word_list = paragraph_lower_no_punctuation.split(" ")

    word_freq = {}
    for word in word_list:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq


def find_max_value(pdict):
    max_key = ""
    max_value = 0
    for key in pdict:
        if pdict[key] >= max_value:
            max_key = key
            max_value = pdict[key]
    return max_key


def sort_words(paragraph):
    words = []
    freqs = get_freq(paragraph)
    x = len(freqs)
    for i in range(x):
        key = find_max_value(freqs)
        words.append(key)
        del freqs[key]
    return words;


print(sort_words("It was a beautiful day in New York City. Our hero Ariana Grande was on a walk from the Standard" 
                 " to Duane Reade. Ariana Grande was walking rather quickly because she had lived in New York for " 
                 "a few months. All of a sudden a slimy donut appeared out of nowhere. Ariana Grande decided to" 
                 " prance foolishly instead of dealing with the situation. Thrown off from Duane Reade Ariana" 
                 " Grande decides to go to Times Square instead. What a beautiful day in New York."))