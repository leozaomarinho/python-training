aluno = {
    'nome': 'leo',
    'idade': 18,
    'masculino' : True,
    'materias': ['fisica','Ed Fisica','matematica']
}


print(aluno['nome'])

#trabalhando com dicionarios em python

aluno['nome'] = 'leonardo'

aluno.update({'idade': 22, 'nome':'leonardo luiz'})
aluno.update({'estado-civil':'solteiro','empregado':True})

print(aluno)
print()

print(aluno.get('estado-civi', 'Valor não encontrado'))

del aluno['masculino']

print(aluno)
print()

aluno.update({'estado-civil':'casado'})

for alun in aluno.values():
    print(alun)
    

  
print()

for alun in aluno.keys():
    print(alun)
    
print()

for keys, values in aluno.items():
    print(keys,values)

print()

print(f'O nome de valores no dicionario aluno é {len(aluno)}')

print(aluno.keys)
print(aluno.items)
print(aluno.values)