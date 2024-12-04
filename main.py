from soma import somar
from subtrair import subtrair
from multiplicar import multiplicar

while True:
    menu = input('1 - Somar \n2 - Subtrair \n3 - Multiplicar \n0 - Sair \n')
    if menu == '1':
        num1 = float(input('Digite um Numero: '))
        num2 = float(input('Digite um Numero: '))
        print(somar(n1=num1, n2=num2))
    elif menu == '2':
        num1 = float(input('Digite um Numero: '))
        num2 = float(input('Digite um Numero: '))
        print(subtrair(n1=num1, n2=num2))
    elif menu == '3':
        num1 = float(input('Digite um Numero: '))
        num2 = float(input('Digite um Numero: '))
        print(multiplicar(n1=num1, n2=num2))
    elif menu == '0':
        break
    
