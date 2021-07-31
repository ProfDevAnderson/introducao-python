# Estrutura condicional
idade = int(input('Qual a sua idade? '))

if idade >= 18:
    print('Você ja pode ser preso')
else:
    print('Tu é de menor ainda kkkkkkkkk')

usuario = input('Digite seu email: ')
senha = input('Digite sua senha: ')

if (usuario == 'andplay@gmail') and (senha == '12345'):
    print('Entrando...')
else:
    print('Usuário ou senha incorreta')
idade = int(input('Qual a sua idade? '))

if idade >= 18 and idade < 65:
    print('Voto Obrigatório')
elif (idade >= 16 and idade <= 17) or idade >=65:
    print('Voto Facutativo')
else:
    print('Você nao pode Votar! Xispa daqui')
