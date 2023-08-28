#1) Faça um Programa que peça dois números e imprima o maior deles.
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

if numero1 > numero2:
    print(f'O número {numero1} é o maior.')
else:
    print(f'O número {numero2} é o maior.')

#2) Faça um Programa que pergunte em que turno você estuda.Peça para digitar 
# M-matutino ou V-Vespertino ou N-Noturno.
# Imprima a mensagem "Bom Dia!","Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!",conforme o caso

turno = input('Em que turno você estuda: M-Matutino, V-Vespertino ou N-Noturno? ')

if turno =='M':
  print('Bom dia!')
elif turno =='V':
  print('Boa tarde!')
elif turno =='N':
  print('Boa Noite!')
else:
  print('Valor Inválido!')

#3) Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
# seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input('Digite uma nota de zero a dez: '))
while nota<0 or nota>10:
    nota = float(input('Digite uma nota de zero a dez: '))
print('A nota digitada é válida!')

