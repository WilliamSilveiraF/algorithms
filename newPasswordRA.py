turns = int(input())
sequences = ["GQaku", "ISblv", "EOYcmw", "FPZdnx", "JTeoy", "DNXfpz", "AKUgq", "CMWhr", "BLVis", "HRjt"]
for turn in range(turns):
    sentence = input().replace(" ", "")
    myPassword = ""
    for letter in sentence:
        for index, sequence in enumerate(sequences):
            if letter in sequence:
                myPassword += str(index)
    print(myPassword[0:12])
