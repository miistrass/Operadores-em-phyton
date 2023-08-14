num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
operacao = input("Qual operação quer fazer? S - Soma, M - Multiplicação, SS - Subtração ou D - Divisão ")

if operacao == "S":
    res = num1 + num2 
    print(f"Você escolheu somar e o resultado é: {res}")
elif operacao == "M":
    res = num1 * num2
    print(f"Você escolheu multiplicar e o resultado é: {res}")
elif operacao == "SS":
    res = num1 - num2
    print(f"Você escolheu subtrair e o resultado é: {res}")
else:
    res = num1 / num2
    print(f"Você escolheu dividir e o resultado é: {res}")