num = int(input('Digite um valor: '))


veri = lambda num : 'par' if num %2==0 else 'impar'
#lambda com if else

print(f'o {num} é {veri(num)}')


