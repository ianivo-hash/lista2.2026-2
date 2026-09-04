int('1-soma')
print('2- subtracao')
print('3- multiplicacao')
print('4-divisao')

x = int(input('escolha uma opcao: '))

a= float(input('digite o primeiro numero'))
b = float(input('digite o segundo numero'))

if x == 1: 
  print('resultado: ', a+b)

elif x == 2: 
  print('resultado: ', a-b)

elif x == 3:
  print('resultado: ', a*b)

elif x == 4:
  print('resultado: ', a/b)

else:
  print('opcao invalida')

      
