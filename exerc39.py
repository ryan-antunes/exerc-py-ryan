num = int(input("Digite um numero: "))
unidade = num/1
dezena = num/10
centena = num/100
if (num<=1000):
  print(f"{num} = {unidade}, {dezena} e {centena}")