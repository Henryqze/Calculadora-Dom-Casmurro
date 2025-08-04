def menu():
    lista = {
        1: "soma",
        2: "subtração",
        3: "divisão",
        4: "multiplicação",
        5: "sair"
    }
    for k, v in lista.items():
        print(f"{k} - {v}")


print("Bem-vindo a calculadora Dom Casmurro.")

while True:
    try:
        print("=-="*40)
        menu()
        print("=-="*40)
        escolha = int(input("Escolha uma opção: "))
        match escolha:
            case 1:
                print("Escolheu a opção de soma.")
                num1 = float(input("Digite um número: ").replace(",", "."))
                num2 = float(input("Digite um número novamente: ").replace(",", "."))
                soma = num1 + num2
                print(f"seu resultado de {num1} + {num2} é {soma}")
                continue
            case 2:
                print("Escolheu a opção de subtração.")
                num1 = float(input("Digite um número: ").replace(",", "."))
                num2 = float(input("Digite um número novamente: ").replace(",", "."))
                subtração = num1 - num2
                print(f"A resultado de {num1} - {num2} é {subtração}")
                continue
            case 3:
                print("Escolheu a opção de divisão.")
                num1 = float(input("Digite um número: ").replace(",", "."))
                num2 = float(input("Digite um número novamente: ").replace(",", "."))
                divisão = num1 / num2
                print(f"A resultado de {num1} / {num2} é {divisão}")
            case 4:
                print("Escolheu a opção de multiplicação.")
                num1 = float(input("Digite um número: ").replace(",", "."))
                num2 = float(input("Digite um número novamente: ").replace(",", "."))
                multiplicacao = num1 * num2
                print(f"A resultado de {num1} x {num2} é {multiplicacao}")
            case 5:
                sair = input("Deseja sair: ")
                if sair == "s":
                    exit()
                elif sair == "n":
                    continue
                else:
                    print("Não compreendi, tente novamente.")
            case _:
                print("Não existe essa opção, tente novamente.")
    except ValueError:
        print("Erro, tente novamente.")