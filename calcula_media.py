numeros = []
#Ler entradas
for i in range(5):
    num = float(input(f'Digite o {i+1}º número: ' ))
    numeros.append(num)
soma = sum(numeros)
media = soma / len(numeros)
print(f'{media:.2f}')
