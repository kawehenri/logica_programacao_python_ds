nome = 'Kawê'
idade = 25


#peso = input('Digite seu peso: ')

num1 = input('Digite o primeiro numero: ')
num1 = int(num1)

num2 = int(input('Digite o segundo numero: '))

# Operadores matematicos
soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
divi = num1 / num2 
divi_int = num1 // num2
expo = num1 ** num2 
modulo = num1 % num2 # resto da divisão

#FIXME - Operadores comparativos

print('Operadores comparativos')
print(num1 > num2) # maior que
print(num1 < num2) # menor que
print(num1 == num2) # igualdade
print(num1 != num2) # diferente
print(num1 <= 100) # menor ou igual

print(num1 <=100 and num2 <= 100 or (num1 + num2) > 100)


#FIXME - Operadores Matematicos

print('Operadores matematicos')
print(num1 + num2)
print(num1 - num2)
print(num1 / num2)
print(num1 * num2)

#FIXME Atribuição de valores 
print('Atribuição de valores')
num1 += 1
num1 -= 1 
num1 /= 1
num1 *= 1 


print(f'soma: {soma}')
print(f'subtração: {sub}')
print(f'multiplicação: {mult}')
print(f'Divisão: {divi}')
print(f'Divisão formatada: {divi:.2f}')
print(f'Divisão inteira: {divi_int}')
print(f'Exponete: {expo}')
print(f'modulo: {modulo}')
print()
print(f'O numero digitado + 1 é: {num1}')

