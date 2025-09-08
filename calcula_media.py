#Lista para armazenar os números
numeros = []

#Ler entradas
for i in range(5):
    
    #Solicita numero e converte para float
    num = float(input(f'Digite o {i+1}º número: ' ))
    numeros.append(num) #Adiciona o número na lista
    
#Calacula a soma de todos números
soma = sum(numeros)
media = soma / len(numeros) #Calcula média

#Mostra resultado
print(f'{media:.2f}')
