cases = int(input())

story = []
for _ in range(cases):
    register = input()
    story.append(register)

story = set(story)

print(len(story))
