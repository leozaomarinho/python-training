

def soma(*numeros):
    resultado =0
    
    #o for foi utilizado para somar os valores, seria como percorrer um array adicionando os valores a uma variavel
    for num in numeros:
        resultado+=num
    return resultado

x = soma(6,6,4,4)

print(x)

