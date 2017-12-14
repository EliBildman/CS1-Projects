paragraph = "It was a beautiful day in New York City. Our hero Ariana Grande was on a walk from the Standard" \
                    " to Duane Reade. Ariana Grande was walking rather quickly because she had lived in New York for " \
                    "a few months. All of a sudden a slimy donut appeared out of nowhere. Ariana Grande decided to" \
                    " prance foolishly instead of dealing with the situation. Thrown off from Duane Reade Ariana" \
                    " Grande decides to go to Times Square instead. What a beautiful day in New York."

# make all letters lowercase
paragraph_lower = paragraph.lower()

# remove all periods
paragraph_lower_no_punctuation = paragraph_lower.replace(".", "")

# convert paragraph into a list of individual strings
word_list = paragraph_lower_no_punctuation.split(" ")

word_freq = {}
for word in word_list:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

while True:
    word = input("What word would you like to know the frequency of? ").lower()
    if word in word_freq:
        print("'" + word + "' occurs " + str(word_freq[word]) + " times")
    else:
        print("'" + word + "' does not occur")
