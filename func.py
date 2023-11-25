#DRY dont repeat yourself
#Funções 

laptop =4

nome = str(input('Digite o seu nome:'))


def verificaEstoque(nome,laptop):
    
    if laptop>0:
        print(f'Olá {nome} você pode retirar um laptop do estoque para o seu uso, há {laptop} disponíveis.')
    else:
        print(f'Olá {nome}, não temos laptops disponíveis para uso nesse momento.')
 #FimFunçãoEmprestimoLaptop       


def atualizaEstoque(laptop):
    
    if laptop !=0:
        laptop-=1
        print(f'Estoque atualizado, há {laptop} em estoque.')
    else:
        print(f'Não há laptops disponíveis em estoque.')

#FimFunçãoAtualizaEstoque
print()        
verificaEstoque(nome,laptop)
print()
atualizaEstoque(laptop)
    
    
    
    


