adicao = 10 + 10
print("Adição: ",adicao)

subtracao = 10 - 5
print("Subtração: ",subtracao)

multiplicacao = 10 * 10
print("Multiplicação: ",multiplicacao)

divisao = 10 / 2.2 #float
print("Divisão: ",divisao)

divisao_inteira = 10 // 2.5 #trunca o número ou retorna inteira
print("Divisão inteira: ",divisao_inteira)

exponenciacao = 2**10 #trunca o número ou retorna inteira
print("Exponenciação: ",exponenciacao)

modulo = 16 % 5 #trunca o número ou retorna inteira
print("Módulo: ",modulo)

# peculiaridade de sinais

concatenacao = 'a' + 'b' + 'c'
print(concatenacao)

    # repetição
a_dez_vezes = 'A'*10
tres_vezes_luiz = 3* 'Luiz'
print(a_dez_vezes)
print(tres_vezes_luiz)

# precedencia de operadores
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + - 

conta_1 = 1 + 1 ** 5 + 5 #1024
print(conta_1) # deu errado por erro de precedencia de operadores

conta_2 = (1 + 1) ** (5 + 5)#1024
print(conta_2) # deu errado por erro de precedencia de operadores