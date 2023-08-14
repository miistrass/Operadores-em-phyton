salario = float(input("Insira o seu salário: "))

if salario < 5000:
    abono = salario * 0.15
    print(f"Seu abono será de: R${abono:.2f}")
else:
    abono = salario * 0.1
    print(f"Seu abono será de: R${abono:.2f}")