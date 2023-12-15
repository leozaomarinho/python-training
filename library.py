from livro import Livro
from solicitante import solicitante

class Library:
    def __init__(self):
        self._livros =[]
        
        def adicionar_livro(self):
            nome = input('Digite o nome do livro: ')
            categoria = input('Digite a categoria do livro: ')
            disponivel = True
            new_livro = Livro(nome, categoria, disponivel)
            self._livros.append(new_livro)
            
        def listar_livros(self):
            for livro in self._livros:
                print(livro)
        
    
    def solicitar_livro(self,solicitante,titulo_livro):
        for livro in self._livros:
            if livro.nome == titulo_livro and livro.disponivel == True:
               if solicitante.livro_pend is None:
                   solicitante.livro_pend = titulo_livro
                   livro.disponivel = False
                   print(f'O {solicitante.nome} solicitou o livro {livro.nome}')
               else:
                   print(f'O {solicitante.nome} já esta com um livro de entrega pendente.')

                   