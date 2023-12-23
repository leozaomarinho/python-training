from library import Library
from solicitante import Solicitante
from livro import Livro

class Program():
    
    @classmethod
    def main(self):

        biblioteca =Library()
        nome_solicitante = input('Qual o seu nome: ')
        locatario = Solicitante(nome_solicitante)

        while True:

            print('O que você deseja fazer: ')
            print('1 - pegar livro emprestado.')
            print('2 - listar livros disponiveis.')
            print('3 - devolver livro.')
            print('4 - cadastrar livro.')
            print('0 - sair.')

            opcao = input('Digite o numero da opcao desejada (0 a 3): ')
            
            if opcao == 1:
                biblioteca.solicitar_livro(locatario)
                
            elif opcao ==2:
                biblioteca.listar_livros()
                
            elif opcao ==3:
                biblioteca.devolver_livro(locatario)
                    
            elif opcao == 4:
                biblioteca.adicionar_livro()
        



        
