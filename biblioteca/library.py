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
            
    def listar_livros(self):
            for livro in self._livros:
                print(livro)
        
    
    def solicitar_livro(self,solicitante:Solicitante,):
    