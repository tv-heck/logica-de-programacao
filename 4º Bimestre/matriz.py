matriz = [
    [3, 8, 1],
    [4, 9, 6],
    [2, 7, 5]
]

print("--- Exibição da Matriz Original ---")
for l in range(3):
    for c in range(3):
        print(matriz[l][c], end=" ")
    print()

print("-"*45)
print(f"Elementos da linha 0 e coluna 1: {matriz[0][1]}")
print(f"Elementos da linha 2 e coluna 2: {matriz[2][2]}")

soma_diagonal = 0

for l in range(3):
    for c in range(3):
        if l == c:
            soma_diagonal += matriz[l][c]
print(f"Soma dos elementos da diagonal principal: {soma_diagonal}")