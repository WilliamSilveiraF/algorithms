cases = int(input()) #colete a quantidade de inputs

for _ in range(cases):
    text = input().split(" ") #transforme meu texto em um array de palavras
    word = input() #a word que a posição precisa ser contada
    countChar = 0 #contador de caracteres já passados
    result = ""
    while len(text) > 0: #faz o loop para manter o contador de posições funcionando caso tenha palavras iguais para a posição ser contada
        if not(word in text): #se a palava não está mais no texto, o loop é quebrado
            break

        for idx, wordIntext in enumerate(text): #analiso cada palavra do meu texto
            text = text[1:] #excluo a palavra analisada no momento

            if word == wordIntext: #se a palavra analisada é igual a palavra que quero contar, chega a hora de setar meu resultado
                if result != "": #Se ele é diferente de "" significa que já existiu uma palavra igual à esse analisada
                    result += f" {countChar + len(word) + 1}" #assim somando a minha contagem atual de char, o tamanho da minha palavra e o espaço e quebrando o loop
                    break
                result += f" {countChar}" #Do contrário só retorna o que já contei até agora
                break
            for let in wordIntext: #se ainda não chegou minha palavra que quero, vai contar todos os caracteres
                countChar += 1
            countChar += 1 #inclusive o espaço
    if result == "": #se cheguei com o resultado sendo uma string vazia, significa que não existe no meu texto essa palavra retornando -1
        print("-1")
    else:
        print(result.strip()) #do contrário, print o resultado tirando o espaçamento na frente da string botados para fugir do out range
