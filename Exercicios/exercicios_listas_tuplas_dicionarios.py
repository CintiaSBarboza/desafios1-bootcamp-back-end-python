#1) Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a
#média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

lista_notas = []
lista_medias = []

quant_alunos = 10
quant_notas = 4

for aluno in range(quant_alunos): #Criar uma lista com 10 alunos
    lista_notas.append([])
    for nota in range(quant_notas):
        lista_notas[aluno].append(float(input(f'Digite a nota {nota+1} do aluno {aluno+1} ')))

for notas in lista_notas:
    lista_medias.append(sum(notas)/len(notas))

#Contar quantos alunos tem média maior ou igual a 7.
alunos_aprovados = sum(1 for media in lista_medias if media >=7.0)

print(f'O número de alunos com média maior ou igual a 7.0 é {alunos_aprovados}')
#2) Programa nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar 
# o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.
# Dica:lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas

nome = input('Digite seu nome com letras maiúsculas ou minúsculas: ')
nome_maiuscula = nome.upper()
nome_invertido = nome_maiuscula[::-1]
print(nome_invertido)

#3) Escreva um programa em Python que onde todos os valores em um dicionario são emitidos.
#se sim, imprima true. Caso contrário, imprima false.

dicionario = {"Banana": 'fruta', "Moto": 'veículo', "Saia": 'roupa'}
print(dicionario)

valores_emitidos = all(valor for valor in dicionario.values())

if valores_emitidos:
    print('True')
else:
    Print('False')


#4) "Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um 
# crime. As perguntas são: "Telefonou para a vítima?", "Estevenolocaldocrime?", "Morapertodavítima?"
#"Deviaparaavítima?", "Játrabalhoucomavítima?"
#O programa deve no final emitir uam classificação sobre a participação da pessoa no crime
# Seapessoaresponderpositivamente a 2 questões ela deve ser classificada com "Suspeita", entre
# 3 e 4 como "Cúmplice" e 5 "Assassino ". Caso contrário, ele será classificado como "Inocente."

pergunta1 = int(input('Telefonou para a vítima? Digite: 1-Sim ou 0-Não '))
pergunta2 = int(input('Esteve no local do crime? Digite: 1-Sim ou 0-Não '))
pergunta3 = int(input('Mora perto da vítima? Digite: 1-Sim ou 0-Não '))   
pergunta4 = int(input('Devia para a vítima? Digite: 1-Sim ou 0-Não '))
pergunta5 = int(input('Já trabalhou com a vítima? Digite: 1-Sim ou 0-Não '))

somaRespostas = pergunta1 + pergunta2 + pergunta3 + pergunta4 + pergunta5

if somaRespostas<2:
    print('Inocente')
elif somaRespostas == 2:
    print('Suspeita')
elif somaRespostas == 5:
    print('Assassino')
else:
    print('Cúmplice')