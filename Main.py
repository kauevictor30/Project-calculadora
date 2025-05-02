from Opções import *

print('-' * 20)
print('Calculadora for VkS!!!')
print('-' * 20)

num1 = float(input('Primeiro numero: '))
num2 = float(input('Segundo numero: '))
opicao = (input('Opção: '))

if opicao == '+':
    resultado = soma(num1, num2)
    print('A soma foi:', resultado)
elif opicao == '-':
    resultado = subtracao(num1, num2)
    print('A subtração foi:', resultado)
elif opicao == '*':
    resultado = multiplicacao(num1, num2)
    print('A multiplicação foi:', resultado)
elif opicao == '/':
    resultado = divisao(num1, num2)
    print('A divisão foi:', resultado)
else:
    print('Opção aritimética invalida!')