from livro import Livro
from solicitante import Solicitante

class Library:
    def __init__(self):
        self._livros = []
        
    def adicionar_livro(self):
            nome = input('Digite o nome do livro: ')
            categoria = input('Digite a categoria do livro: ')
            disponivel = True
            new_livro = Livro(nome, categoria, disponivel)
            self._livros.append(new_livro)
            
    def listar_livros(self,livro:Livro):
            for livro in self._livros:
                if livro.disponivel:
                    print(livro)
        
    
    def solicitar_livro(self,solicitante:Solicitante,livro:Livro):
        if solicitante.livro_pend == True:
            print('O solicitante não pode haver livros pendentes de devolução.')
        else:
            if livro.disponivel == False:
                print('O livro solicitado não esta disponível.')
            else:
                solicitante.livro_pend = True
                livro.disponivel=False
                solicitante.nome_livro = livro.nome
                print('Emprestimo de livro realizado com sucesso!')