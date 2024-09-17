a = int(input("Digite o valor de 'A': "))
b = int(input("Digite o valor de 'B': "))
c = int(input("Digite o valor de 'C': "))

delta = 0

if(a == 0):
  print("Essa equação é de segundo grau")
else:
  delta = (b*b) - (4*a) * c
  if (delta < 0):
    print("Essa equação não possui raizes. ")
  elif(delta==0):
    print("Essa equação possui apenas raíz real. ")
  else:
    print("A equação possui duas raizes. ")