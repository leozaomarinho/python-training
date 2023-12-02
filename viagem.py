from viagem_class import viagem_class

nome_viajante = input('Digite seu nome para começarmos: ')

print(f'Olá {nome_viajante}, escolha um destino que combine com você: ')

print(f'1 - Florida')
print(f'2 - Veneza')
print(f'3 - Londres')
print(f'4 - Maldivas')
print(f'5 - Toquio')

option = int(input('Digite de 1 a 5 qual será o seu destino: '))

if option==1:
    destino ='Florida'
    viagem = viagem_class(destino,nome_viajante)
elif option==2:
    destino='Veneza'
    viagem = viagem_class(destino,nome_viajante)
elif option==3:
    destino='Londres'
    viagem = viagem_class(destino,nome_viajante)
elif option==4:
    destino='Maldivas'
    viagem = viagem_class(destino,nome_viajante)
elif option==5:
    destino='Toquio'
    viagem = viagem_class(destino,nome_viajante)
else:
    print('Digite uma opção valida.')
    
print(f'parabens {viagem.nome_viajante} você vai visitar {viagem.destino} ')
    
    



