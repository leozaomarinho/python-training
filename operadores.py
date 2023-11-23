num = 2
num2= 8
num3 =8

result = num2 >num or  num2 > num3

print(result)

if num3>num2:
    print(f'{num3} é maior que {num2}')
    
    
#fimDoIf   
elif num3==num2:
    print('Os dois possuem o mesmo valor.')


#elseIf em python é assim
#fimDoElif
else:
    print(f'{num3} é menor que {num2}')
    
#fimDoElse