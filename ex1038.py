#Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item.
#A seguir, calcule e mostre o valor da conta a pagar.

if __name__ == '__main__':
  cod, qt = input().split()
  cod = int(cod)
  qt = int(qt)
  if (cod == 1):
      total = qt * 4
  elif (cod == 2):
      total = qt * 4.5
  elif (cod == 3):
      total = qt * 5
  elif (cod == 4):
      total = qt * 2
  elif (cod == 5):
      total = qt * 1.5
  print(f'Total: R$ {total:.2f}')

