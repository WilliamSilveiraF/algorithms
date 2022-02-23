cases = int(input())

story = []
for _ in range(cases):
    register = input() #pegue todos os registros
    story.append(register)

story = set(story) #filtre todos os registros sem repetição

print(len(story))
