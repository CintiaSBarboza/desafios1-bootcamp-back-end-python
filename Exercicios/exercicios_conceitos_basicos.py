#1)Faça um Programa que peça um número e então mostre a mensagem:->O númeroinformadofoi[número].
numero = int(input('Digite um número: '))
print(f'O número informado foi {numero}.')


#2)Faça um programa que peça dois números e imprima a soma.
numero1 = int(input('Digite o número 1:'))
numero2 = int(input('Digite o número 2:'))
soma = numero1 + numero2
print(f'A soma dos números digitados é {soma}.')


#3) Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit
temperaturaCelsius = float(input('Digite a temperatura de hoje:'))

temperaturaFahrenheit = ((temperaturaCelsius * 9)/5) + 32
print(f'A temperatura em Fahrenheit é {temperaturaFahrenheit}ºF.')


#4) Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calule e mostre o total do seu salário no referido mês.
salarioHora = float(input('Quanto você ganha por hora trabalhada? '))
horasTrabalhadasMes = int(input('Quantas horas você trabalhou esse mês? '))
salario = salarioHora * horasTrabalhadasMes
print(f'O seu salário esse mês foi de R$ {salario:.2f}')
