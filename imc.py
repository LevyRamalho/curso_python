nome = 'Levy'
peso = 50
altura = 1.70
imc = peso/(altura ** 2)

print(imc)

print(nome, 'tem ', altura, 'de altura. Pesa ', peso, ' quilos e seu IMC é ', imc )
# f-strings
print(f'{nome} tem  {altura} de altura. Pesa  {peso}  quilos e seu IMC é {imc :.2f}')

# ... ellipsis