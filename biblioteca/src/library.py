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
            
            print(f"Livro cadastrado com sucesso!\n")
            
    def listar_livros(self,livro:Livro):
            print("----- Lista de livros -----")
            for livro in self._livros:
                if livro.disponivel:
                    print(livro)
            print("\n")
        
    
    def solicitar_livro(self,solicitante:Solicitante,livro:Livro):
        if solicitante.livro_pend == True:
            print('O solicitante não pode haver livros pendentes de devolução.')
        else:
            if livro.disponivel == False:
                print('O livro solicitado não esta disponível.')
            else:
                if livro in self._livros:
                    solicitante.livro_pend = True
                    livro.disponivel=False
                    solicitante.nome_livro = livro.nome
                    print('Emprestimo de livro realizado com sucesso!')
                    
    def devolver_livro(self,Solicitante:Solicitante):
        livroDevo = input('Digite o nome do livro que esta sendo devolvido: ')
        if livroDevo in self._livros:
            Solicitante.livro_pend = False
            for livro in self._livros:
                livro == livroDevo
                print('Livro devolvido com sucesso.')
        else:
            print('O Livro que você esta tentando devolver não é valido, digite o nome correto.')