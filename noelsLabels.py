test = int(input())

dictionary = {}

for _ in range(test):
    languange = input()
    dictionary[languange] = input()

childs = int(input())

for _ in range(childs):
    print(input())
    print(f"{dictionary[input()]}\n")
