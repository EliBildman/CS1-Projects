memes = {"nbd": "no big deal", "tbd": "to be determined", "lol": "laugh out loud"}

while True:
    word = input("Word to look up/'update': ")
    if word == "update":
        word = input("Word to update: ")
        memes[word] = input("New definition: ")
    else:
        if word in memes:
            print(word + ": " + memes[word])
        else:
            if input("Sorry, '" + word + "' is not defined, would you like to define it? (y/n): ") == 'y':
                memes[word] = input("Definition: ")

