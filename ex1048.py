#A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:
#Salário	Percentual de Reajuste
#0 - 400.00
#400.01 - 800.00
#800.01 - 1200.00
#1200.01 - 2000.00
#Acima de 2000.00
#15%
#12%
#10%
#7%
#4%
#Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

if __name__ == '__main__':

    salario = float(input("Digite o salário do funcionário: "))

    if salario <= 400.00:
        percentual = 0.15
    elif salario <= 800.00:
        percentual = 0.12
    elif salario <= 1200.00:
        percentual = 0.10
    elif salario <= 2000.00:
        percentual = 0.07
    else:
        percentual = 0.04
    r = salario * percentual
    ns = salario + r
    p = percentual * 100

    print(f"Novo salário: R$ {ns:.2f}")
    print(f"Reajuste ganho: R$ {r:.2f}")
    print(f"Em percentual: {p:.0f}%")
