qtd = 0
ass = []
print("Responda com 's' ou 'n'\n")
print("s-sim e n-não\n")
ass.append(input("O senhor/a telefonou para a vítima?\n").lower())
ass.append(input("E esteve no local do crime?\n").lower())
ass.append(input("Mora perto da vítima?\n").lower())
ass.append(input("Devia para a vítima?\n").lower())
ass.append(input("Trabalhou com a vítima\n").lower())

qtd = ass.count('s')

if (qtd>=5):
  print("Assasino")
elif (qtd>=3):
  print("Cúmplice")
elif (qtd>=2):
  print("Suspeito")
else:
  print("Inocente")