# Matriz é uma lista de lista
Matriz = [
    [0,1,2],
    [5,8,7],
    [2,3,7]
]
# print(Matriz[0][0])
# print(Matriz[0][1])
# print(Matriz[0][2])
# print(Matriz[1][0])

# Definir dois laços, um para percorrer a linha e outro a coluna

for i in range(3):
    for j in range(3):
        print(Matriz[i][j], end = "|")
    print('')

linha = int (input("Quantidade de linhas: "))
coluna = int (input("Quantidade de Colunas"))

M = []
for i in range(linha):
    novaLinha = []
    for j in range(coluna):
        num = int(input('Valor: '))
        novaLinha.append(num)
    M.append(novaLinha)
print(M)

for i in range(linha):
    for j in range(coluna):
        print(M[i][j], end = "|")
    print('')

