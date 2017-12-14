memes = {"nbd": "no big deal", "tbd": "to be determined", "lol": "laugh out loud"}

while True:
    word = input("What word would you like to look up? ")
    if word in memes:
        print(word + ": " + memes[word])
    else:
        print("Sorry " + word + " is not defined")
