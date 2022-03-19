rows = int(input()) 

butterflies = [] 
matrix = [] 
for _ in range(rows): 
    row = list(map(int, input().split(' ')))
    matrix.append(row)

for _ in range(rows * 2): 
    x, y = list(map(int, input().split(' '))) 
    x -= 1 
    y -= 1
    for idx, row in enumerate(matrix): 
        if idx == x:
            for yIdx, butterfly in enumerate(matrix[idx]):
                if yIdx == y:
                    butterflies.append(butterfly)

print(len(set(butterflies))) 