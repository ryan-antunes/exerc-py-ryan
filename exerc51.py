num = int(input("Digite um número: "))
if num > 1:
  for i in range(2, num):
    if num % i == 0:
      print(num, 'Não é primo')
      break
  else:
      print(num, 'É primo')
elif num == 0:
      print(num, 'É zero')
elif num == 1:
      print(num, 'É um')
else:
      print(num, 'É negativo')