import time

def tempo():
    mensagem = "Retornando para o menu..."
    for x in mensagem:
        time.sleep(0.3)
        print(x, end='', flush=True)
    print()

        
def menu():
    menu = {
        1: "soma",
        2: "subtração",
        3: "divisão",
        4: "multiplicação",
        5: "sair"
    }
    print("=-="*40)    
    print("Bem-vindo a calculadora Dom Casmurro.")
    print("=-="*40)
    for k, v in menu.items():
        print(f"{k} - {v}")

def lendo(mensagem):
    while True:
        try:
            valor = input(mensagem).replace(',','.')
            return float(valor)
        except ValueError:
            print("Entradas inválidas, tente novamente.")
    
def contas(operacao, num1, num2):
    match operacao:
        case 1:
            return num1 + num2
        case 2:
            return num1 - num2
        case 3:
            if num2 == 0:
                return "Error: Divisão por zero"
            return num1 / num2
        case 4:
            return num1 * num2
while True:
    menu()
    try:
        escolha = int(input("Escolha uma opção: "))
    except ValueError:
        print("Erro, tente novamente.")
        continue
    match escolha:
        case 5:
            print("Saindo...")
            break
        case 1 | 2 | 3 | 4:
            num1 = lendo("Digite um número: ")
            num2 = lendo("Digite um número: ")
            total = contas(escolha, num1, num2)
            print(f"O resultado da sua conta foi {total}")
            tempo()
        case _:
            print(f"A opção {escolha} não foi encontrada, tente novamente.")