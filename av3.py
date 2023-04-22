#3) Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva a
#média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores
#negativos e o percentual de valores negativos e positivos.
soma = 0
qtd_positivos = 0
qtd_negativos = 0

while True:
    valor = float(input("Digite um valor (ou 0 para sair): "))
    if valor == 0:
        break
    if valor > 0:
        qtd_positivos += 1
    else:
        qtd_negativos += 1
    soma += valor

total_valores = qtd_positivos + qtd_negativos
media = soma / total_valores
percent_positivos = (qtd_positivos / total_valores) * 100
percent_negativos = (qtd_negativos / total_valores) * 100

print("Média: %.2f" % media)
print("Quantidade de valores positivos: %d" % qtd_positivos)
print("Quantidade de valores negativos: %d" % qtd_negativos)
print("Percentual de valores positivos: %.2f%%" % percent_positivos)
print("Percentual de valores negativos: %.2f%%" % percent_negativos)