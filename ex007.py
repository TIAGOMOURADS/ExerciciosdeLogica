#Leia quatro valores inteiros A, B, C e D.
#A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

if __name__ == '__main__':

    a = int(input('Digite um número: '))
    b = int(input('Digite um número: '))
    c = int(input('Digite um número: '))
    d = int(input('Digite um número: '))
    df = a * b - c * d
print('DIFERENÇA = ', df)
