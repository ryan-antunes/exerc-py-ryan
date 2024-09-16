salario_base = int(input("Digite o salario base: "))
imposto = (7*salario_base/100)
gratificação = (5*salario_base/100)
salario_a_receber = salario_base + gratificação - imposto
print ("O salario a receber é: ", salario_a_receber)