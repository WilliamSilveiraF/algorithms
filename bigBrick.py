alphabet = [[" "], [], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"],
            ["t", "u", "v"], ["w", "x", "y", "z"]] # faço meu alfabeto para colher os índices relacionados às teclas do celular na função quando procurar por letra

def getCodeByLetter(letter): #
    result = ""
    if letter.isupper(): #se a letra que eu procuro é maiúscula já coloco o # conforme o enuciado
        result += "#"
    letter = letter.lower() #puxo a letra analisada para minúscula para pesquisar no meu arr com índices de teclas
    for idx, button in enumerate(alphabet): #Cada letra de cada botão do meu celular vai ser percorrido para pegar quantas vezes, eu preciso aperta uma certa tecla para chegar na letra que quero
        if letter in button:
            for isMyLetter in button:
                result += str(idx) #Passo o índice para string
                if letter == isMyLetter: #se eu achei a letra que quero, meu lop quebra para não contar mais o índice do botão
                    break
    return result #retorno o código para aquela letra

cases = int(input()) #pego a quantidade de meus inputs

for _ in range(cases):
    word = input() #pega a minha palavra para ser decifrada
    alreadyAnalysedCode = " " #variáveis de controle para verificar se um número é repetido na tecla por ex, bota o espaço para fugir do erro out of range, tira depois com strip
    code = " "

    for let in word:
        letterCode = getCodeByLetter(let) #uso minha função auxiliar para pegar o código daquela letra
        if alreadyAnalysedCode[-1] == letterCode[-1]: #se meu código atual, for igual ao último analisado significa que estão na mesma tecla
            if letterCode[0] == "#": #se estão na mesma tecla, mas a nova letra é maiúscula não usaremos o * para representar que ficamos segurando a tecla
                code = f"{code}" + f"{letterCode}"
            else: #do contrário, iremos usar o * para representar a manutenção da tecla pressionada
                code = f"{code}" + "*" + f"{letterCode}"
        else:
            code = f"{code}" + f"{letterCode}" #Mas se a letra está em uma tecla diferente, não tem necessidade de representar o "*", assim então só adiciona o código da função ao nosso resultado
        alreadyAnalysedCode += letterCode
    print(code.strip()) #strip para remover o primeiro espaço que colocamos
