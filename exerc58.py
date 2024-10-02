porcentagem = 0
preço = 0
desconto = 0
valor = 0
print("a para Álcool\n")
print("g para Gasolina\n")
tipoc = (input("Tipo do combustivel: ").lower())
l = float(input("Digite a quantidade de litros: ")) 
if (tipoc == 'a'):
  if(l<=20):
    porcentagem = l*3
    preço = l*3.90
    desconto = (preço-desconto)/100
    valor = preço-desconto
  else:
    porcentageml = l*5
    preço = l*3.90
    desconto = (preço*porcentagem)/100
    valor = preço-desconto
elif(tipoc=='g'):
  if(l<=20):
    porcentagem = l*4
    preço = l*5.50
    desconto = (preço*porcentagem)/100
    valor = desconto-preço
  else:
    porcentagem = l*6
    preço = l*5.50
    desconto = (preço*porcentagem)/100
    valor = desconto-preço
else:
  print("Tipo de combustivel errado: ")
print(f"Irá pagar R$ {valor}")