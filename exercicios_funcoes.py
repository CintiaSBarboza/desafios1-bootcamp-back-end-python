#1) Faça um programa,com uma função que necessite de três argumentos, e que forneça a soma desses 
#três argumentos.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

def soma():
    calculo = num1+num2+num3
    print(f'A soma dos número é {calculo}.')

soma()

#2) "Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado.
# Por exemplo:127->721.

def reverso(numero):
    return  str(numero[::-1])

numero = (input('Digite um número: '))
print(reverso(numero))

#3) Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau
# Celsius para Fahrenheit ou vice-versa. Para cada opção,crie uma função.
# Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu 
# chama a função de conversão correta.

def Celsius_para_F(C):
    F = (C*9/5) + 32
    return F

def F_para_Celsius(F):
    C = (F-32)*5/9
    return C

def menu():
    print('Escolha uma opção:')
    print("1 - Converter de Celsius para Fahrenheit")
    print("2 - Converter de Fahrenheit para Celsius")
    escolha = input("Digite a opção escolhida: ")
    return escolha

escolha = menu()

if escolha =="1":
    C = float(input('Digite a temperatura em graus Celsius: '))
    fahrenheit = Celsius_para_F(C)
    print(f'A temperatura em Fahrenheit é {fahrenheit}ºF.')

elif escolha =="2":
    F = float(input('Digite a temperatura em graus Fahrenheit: '))
    celsius = F_para_Celsius(F)
    print(f'A temperatura em Celsius é {celsius}ºC.')
else:
    print('Opção inválida')
