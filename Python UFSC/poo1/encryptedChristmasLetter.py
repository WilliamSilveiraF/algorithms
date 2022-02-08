while True:
    try:
        result = ''
        phrase = input()
        newWord = phrase.replace("@", "a").replace("&", "e").replace("!", "i").replace("*", "o").replace("#", "u")
        print(newWord)
    except EOFError:
        break
