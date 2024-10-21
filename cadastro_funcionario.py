#id
#nome_completo
#cpf
#profissao
#area
#salario
#bonificacao

id = int(input("digite sua matricula: "))
nome_completo = str(input("seu nome completo: "))
cpf = int(input("seu cpf: "))
profissao =str(input("profissão: "))
area = str(input("area: "))
salario = float(input("Salario: "))
bonificacao = float(input("bonificaçao: "))
salario_bruto = salario + bonificacao

print("")
print("")

print(f"identificação do funcionario: {id}")
print(f"funcionario: {nome_completo}")
print(f"cpf: {cpf}")
print(f"profissâo: {profissao}")
print(f"area: {area}")
print(f"salario:  {salario}")
print(f" bonificação: {bonificacao}")
print(f"salario bruto:  {salario_bruto}")

print("")
print("fim do programa")
print("")