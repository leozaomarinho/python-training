nome = input("Digite seu nome: ")
idade = input("Qual a sua idade: ")
idade = str(idade) #fazendo o casting do valor int para string
cidade = input("Qual a sua cidade: ")

print(nome)
print(idade)
print(cidade)

print('O ' + nome + ' tem '+ idade +' anos de idade, e mora em '+ cidade)
"""
Testando o comentario
esse teste
"""

anoNascimento = input("Digite o seu ano de nascimento para saber sua idade: ")
idade = 2023 - int(anoNascimento)
print(idade)