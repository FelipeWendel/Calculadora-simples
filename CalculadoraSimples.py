def adiciona(x, y):
    return x + y

def subtrai(x, y):
    return x - y

def multiplica(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Não é possível dividir por zero!")
    return x / y

def calculadora():
    print("Calculadora Simples")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Escolha a operação: ")

    if escolha in ("1", "2", "3", "4"):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == "1":
            print(f"{num1} + {num2} = {adiciona(num1, num2)}")
        elif escolha == "2":
            print(f"{num1} - {num2} = {subtrai(num1, num2)}")
        elif escolha == "3":
            print(f"{num1} * {num2} = {multiplica(num1, num2)}")
        elif escolha == "4":
            try:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ValueError as e:
                print(e)
    else:
        print("Opção inválida!")

calculadora()