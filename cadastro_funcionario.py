print("### MENU ###")

print("\nEscolha uma das opçoes abaixo: ")

print(f"[1] PARA CADASTRO DO FUNCIONARIO ")
print(f"[2] PARA CADASTRO DO CLIENTE")
print(f"[3] PARA CADASTRO DE PRODUTO")
print(f"[4] PARA SAIR")

escolha = int(input("Escolha uma das opçoes: "))


if escolha == 1:    

    print("\n*****Cadastro De Funcionarios:***** ")

    print("")
    print("")

    id = int(input("Digite a matricula: "))
    nome_completo = str(input("Digite o nome completo: "))
    cpf = int(input("Digite o CPF: "))
    profissao =str(input("DIgite a Profissão: "))
    area = str(input("Digite a Area: "))
    salario = float(input("Digite o Salario: "))
    bonificacao = float(input("Digite a Bonificaçao: "))
    salario_bruto = salario + bonificacao

    print("")
    print("")

    print("#####[CADASTRO DE FUNCIONÁRIOS]#####")
    print("") 
    print(f"Identificação do funcionario: [{id}]")
    print(f"Funcionario: [{nome_completo}]")
    print(f"CPF: [{cpf}]")
    print(f"Profissâo: [{profissao}]")
    print(f"Area: [{area}]")
    print(f"Salario: [{salario}]")
    print(f"Bonificação: [{bonificacao}]")
    print(f"Salario bruto: [{salario_bruto}]")

if escolha == 2:
    print("Projeto em fase de desenvolvimento")
    
if escolha == 3:
        print("\n*****CADASTRO DE PRODUTO*****")
        
        print()
        print()
        
        id = int(input("Digite o código do produto: "))
        produto = str(input("Digite o nome do produto: "))
        categoria = str(input("Digite a categoria do produto: "))
        modelo = str(input("Digite o modelo do produto: "))
        marca = str(input("Digite a marca do produto: "))
        pacote = int(input("Digite a quantidade do produto por pacote: "))
        valor = float(input("Digite o valor unitário do produto: "))
        valor_final = pacote * valor
        print()
        
        resultado = int(input("Deseja visualizar o cadastro: \n[1 - para sim] \nou \nclear[0 - para não]: "))
        
        if resultado == 1:
            print(f" CÓDIGO DO PRODUTO: [{id}]")
            print(f" NOME: [{produto}]")
            print(f" CATEGORIA: [{categoria}]")
            print(f" MODELO: [{modelo}]")
            print(f" MARCA: [{marca}]")
            print(f" QDT POR PACOTE: [{pacote}]")
            print(f" VALOR UNITÁRIO: [{valor}]")
            print(f" VALOR FINAL: [{valor_final}]")
    
if escolha == 4:
    print("")
    print("Fim do programa")
    print("")