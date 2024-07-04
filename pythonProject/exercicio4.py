lista = [2,4,6,8,10,11,12]
n = len(lista)
soma = 0

for i in range(n):
    if(lista[i]%2==0):
        soma = soma +lista[i]

print(soma)