n1 = int(input("Digite o seu primeiro número: "))
n2 = int(input("Digite o seu segundo número: "))
n3 = int(input("Digite o seu terceiro número: "))

maior = n1
if n2 > maior:
  maior = n2
if n3 > maior:
  maior = n3

print("O maior número é:", maior)