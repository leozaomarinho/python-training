import math

def verificaSteak(temp):
    
    if temp<48:
        print('Precisa cozinhar mais.')
    
    elif temp in range (48,53):
        print('A carne esta selada.')
        
    elif temp in range(54,59):
        print('Ao ponto para mal.')
        
    elif temp in range(60,64):
        print('Ao ponto.')
        
    elif temp in range(65,70):
        print('Ao ponto para o bem passado.')
        
    elif temp>=71:
        print('Bem passado.')
        
        
#desafio2
"""

def calculaRend(rendimento,altura,largura,capacidadeLata):
    
    capa)
    area = float(largura * altura)
    capacidadeLata = float(capacidadeLata)
    
    quantidadeTinta=float(area/rendimento)
    latasNec = tinta/
    
    return f'Você precisa de {rendimento} latas de tinta para {area} metros quadrados.'
    
"""

def calculaRaiz(num):
    #result=int(num**2)
    
    result = int(math.pow(num,2))
    
    print(f'o quadrado de {num} é {result}')
    
    
def potencia():
    
    base = int(input('Digite o valor da base: '))
    exp = int(input('Digite o valor do expoente ( default =2 ): '))
    
    if exp ==0:
        exp =2
    
    result = int(math.pow(base,exp))
    
    print(f'A base escolhida foi {base}, o expoente foi {exp}, o resultado é : {result}')
    
def calcula_dobro(num):
    
    result = num *2
    print(f'o dobro de {num} é {result}')
    
    print(f'a raiz de {num} {calculaRaiz(num)}')
    
    print(f'a raiz do dobro de {num} é {calculaRaiz(result)}')
    