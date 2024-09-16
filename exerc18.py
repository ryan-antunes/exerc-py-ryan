deposito = float(input("Digite o valor do deposito: "))
taxa_juros = float(input("Digite o valor da taxa: "))

rendimento = deposito * (taxa_juros / 100)
valor_total = deposito + rendimento 

print("rendimento: ", rendimento)
print("valor total: ", valor_total)