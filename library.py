from livro import Livro

class Library:
    def __init__(self,livros:Livro):
        self._livros =[]
        
        def adicionar_livro(self,new_livro):
            self.livros.append(livros)
            
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

                   