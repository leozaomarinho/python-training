friends ={'marcos','artur','leo','hiago','francisco'}
friends2 = {'leo','marcos','thays','alex','karol'}

result = friends.intersection(friends2)
#intersection exibe os valores iguais nas duas listas

print(f'valores iguais nas duas listas : {result}')

uniao = friends.union(friends2)
##ao unir o set ele já remove os duplicados

print()
diferenca = friends.difference(friends2)
print(f'diferença da lista 1 para a 2 {diferenca}')
#diferenca da lista 1 para a 2
diferenca = friends2.difference(friends)
print(f'diferença da lista 2 para a 1 {diferenca}')


print()
print(f'Uniao das duas listas {uniao}')
##

print(type(uniao))