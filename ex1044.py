#Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos",
#indicando se os valores lidos são múltiplos entre si.
if __name__ == '__main__':
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))

    if a % b == 0 or b % a == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")