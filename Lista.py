#Lista
frutas = ['Banana', 'Ata', 'Manga', 'juçarra', 'Pequi', 'Murici', 'Cajá']

print("Frutas que você encontra no MA")
for f in frutas:
    print(f)
print('Removendo o acento...')
frutas[6] = 'Caja'
frutas[3] = 'Juçara'
for f in frutas:
    print(f)
print("A quantidade frutas são: ", len(frutas))


print('---Sistema de Alunos do Andis---')
alunos = []
resposta = 's'
while resposta == 's':
    nome = input("Nome do aluno: ")
    alunos.append(nome)
    resposta = input('Deseja adicionais mais um? [s/n]')

print('Tenho ', len(alunos), ' alunos')
alunos.sort()
print('Lista de Alunos--------')
for a in alunos:
    print(a)

excluir = input('Digite o nome do aluno a ser excluido: ')
alunos.remove(excluir)
print('Lista de Alunos--------')
for a in alunos:
    print(a)
print('Remover por índice: ')
alunos.pop(0)
print('Lista de Alunos--------')
for a in alunos:
    print(a)