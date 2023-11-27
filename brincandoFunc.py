#functions
    #Realizam uma tarefa
    #calcula e retorna um valor

"""
def cliente1(nome):
    print(f'olá {nome}')
    #realiza tarefa de imprimir

cliente1('maria')

def cliente2(nome):
    return f'Olá {nome}'
    #retorna um valor
    
x = cliente1('maria')
y = cliente2('josé')

print(x)
print(y)
#print(cliente2('josé'))

"""

idade = 19
cnh = True

def podeDirigir(idade,cnh):
    if idade>=18 and cnh == True:
        print('A pessoa esta apta a dirigir.')
    else:
        print('A pessoa não esta apta a dirigir')