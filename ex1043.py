#Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo.
#Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:
#Perimetro = XX.X
#Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem
#Area = XX.X

if __name__ == '__main__':

    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

    if a < b + c and b < a + c and c < a + b:
        p = a + b + c
        print("Perimetro = {:.1f}".format(p))
    else:
        at = ((a + b) * c) / 2
        print("Area = {:.1f}".format(at))