alphabet = [[" "], [], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"],
            ["t", "u", "v"], ["w", "x", "y", "z"]]

def getCodeByLetter(letter):
    result = ""
    if letter.isupper():
        result += "#"
    letter = letter.lower()
    for idx, button in enumerate(alphabet):
        if letter in button:
            for isMyLetter in button:
                result += str(idx)
                if letter == isMyLetter:
                    break
    return result

cases = int(input())

for _ in range(cases):
    word = input()
    code = ""
    print(word)
    for let in word:
        letterCode = getCodeByLetter(let)
        if code[-1] == letterCode[-1]:
            code += "*" + letterCode #continuar aqui
        else:
            code += letterCode
    print(code)