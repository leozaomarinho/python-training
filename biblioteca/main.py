import library
import solicitante

biblioteca =library()

nome_solicitante = input('Qual o seu nome: ')
pendencia = False

locatario = solicitante(nome_solicitante,pendencia)

print('O que você deseja fazer: ')
print('1 - pegar livro emprestado.')
print('2 - listar livros disponiveis.')
print('3 - devolver livro.')
print('0 - sair.')

opcao = input('Digite o numero da opcao desejada (0 a 3): ')

if opcao ==1:
    
