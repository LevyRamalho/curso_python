# conversão de Tipos, coerção
# type conversion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutaveis e primitivos: str, int, float, bool


# int transforma em número inteiro
# float transforma em número flutuante

print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(''))

# como o python é uma linguagem de tipagem forte, ele vai gerar um erro quando for fazer uma formulá com tipos diferentes
print(11 + 'b')