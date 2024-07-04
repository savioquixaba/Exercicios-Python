def ehpar(num):
    r= (num%2==0)
    return r

def soma_par(lista):
    soma = 0
    for i in lista:
        if ehpar(i):
            soma += i
    return soma

lista_teste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
somap = soma_par(lista_teste)
print("a soma dos numeros é [{}]".format(somap))
