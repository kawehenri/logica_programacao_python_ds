nome = str(input('Digite o seu nome: '))
email = str(input('Digite o seu email: '))
telefone = input('Digite o seu telefone: ')
pre_gas = float(input('Digite o valor da gasolina: '))
pre_eta = float(input('Digite o valor do alcool: '))
km_dia = 64
aut_gas = 14
aut_eta = 12 

gast_gas_mes = pre_gas*(20*km_dia)/aut_gas
gast_eta_mes = pre_eta*(20*km_dia)/aut_eta
km_mes = km_dia*20
km_gas = km_mes/aut_gas
km_eta = km_mes/aut_eta

print(f'O gasto mensal de gasolina é de {gast_gas_mes:.3f} reais e a quantidade em litro de gasolina será de {km_gas:.2f} litros')
print(f'O gasto mensal de alcool é de {gast_eta_mes:.3f} reais e a quantidade em litro de alcool será de {km_eta:.2f} litros')
print(f'A quantidade de km rodados será de {km_mes} km')