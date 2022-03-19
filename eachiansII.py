cases = int(input()) 

for _ in range(cases):
    text = input().split(" ") 
    word = input() 
    countChar = 0 
    result = ""
    while len(text) > 0: 
        if not(word in text):
            break

        for idx, wordIntext in enumerate(text): 
            text = text[1:] 

            if word == wordIntext: 
                if result != "": 
                    result += f" {countChar + len(word) + 1}" 
                    break
                result += f" {countChar}" 
                break
            for let in wordIntext: 
                countChar += 1
            countChar += 1 
    if result == "":
        print("-1")
    else:
        print(result.strip()) 
