#Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.

if __name__ == '__main__':
    a = int(input('Digite um valor: '))
    b = int(input('Digite outro valor: '))
    c = int(input('Digite outro valor: '))
    if a > b and a > c:
        print(a, 'eh o maior')
    elif b > a and b > c:
        print(b, 'eh o maior')
    elif c > a and c > b:
        print(c, 'eh o maior')




