numero = int(input("Digite um número: "))
if numero > 1:
  for i in range(2, numero):
    if numero % i == 0:
      print(numero, 'Não é primo')
      break
  else:
    print(numero, 'é primo')
elif numero == 0:
  print(numero, 'é zero')
elif numero == 1:
  print(numero, 'é um')
else:
  ptint(numero, 'é negativo')