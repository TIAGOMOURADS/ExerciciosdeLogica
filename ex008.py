#Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora
#e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

if __name__ == '__main__':
    num1 = int(input('Número do funcionário: '))
    num2 = int(input('Horas trabalhadas: '))
    num3 = float(input('Valor que recebe por hora: '))
    sal = num2 * num3
    print('Horas = ', num2)
    print('salario = U$%.2f\n'%(sal))

