#4) Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles
#estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve
#terminar quando for lido um número negativo.
if __name__ == '__main__':
    qtd_intervalo1 = 0
    qtd_intervalo2 = 0
    qtd_intervalo3 = 0
    qtd_intervalo4 = 0

    while True:
        numero = int(input("Digite um número, caso queira encerrar digite um número negativo ): "))
        if numero < 0:
            break
        if numero >= 0 and numero <= 25:
            qtd_intervalo1 += 1
        elif numero >= 26 and numero <= 50:
            qtd_intervalo2 += 1
        elif numero >= 51 and numero <= 75:
            qtd_intervalo3 += 1
        else:
            qtd_intervalo4 += 1

    print("Quantidade de números no intervalo [0-25]: %d" % qtd_intervalo1)
    print("Quantidade de números no intervalo [26-50]: %d" % qtd_intervalo2)
    print("Quantidade de números no intervalo [51-75]: %d" % qtd_intervalo3)
    print("Quantidade de números no intervalo [76-100]: %d" % qtd_intervalo4)
