# Arquivo para demonstrar exemplos de funções em Python
def saudacao():
    print('Olá mundo pelo metodo')

def saudacao_nome(nome):
    print('Olá ', nome)

def soma(numero1, numero2):
    return numero1+numero2

saudacao()
saudacao_nome('Pedro')
numero1 = int(input('Numero 1: '))
numero2 = int(input('Numero 2: '))
resultado = soma(numero1, numero2)
print(resultado)