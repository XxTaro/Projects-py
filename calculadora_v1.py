# Calculadora em Python
print("\n******************* Python Calculator *******************")

print("\nSelecione o tipo de operação que deseja fazer:")
print("\n1 - Soma")
print("2 - Subtração")
print("3 - Divisão")
print("4 - Multiplicação")

opcao = int(input("\nDigite a opção que deseja (1/2/3/4): "))

if opcao > 4:
    print('\n')
    print('\nOpção inválida, tente novamente!')
    print('\n')
    
else:

    a = float(input('\nDigite o primeiro valor: '))
    b = float(input('\nDigite o segundo valor: '))

    if opcao == 1:
        c = a+b
        print('\n')
        print('\n{} + {} = {}'.format(a,b,c))
        print('\n')
        
    if opcao == 2:
        c = a-b
        print('\n')
        print('\n{} - {} = {}'.format(a,b,c))
        print('\n')
    
    if opcao == 3:
        if b==0:
            print('\n')
            print('ERRO! Divisivel igual a 0')
            print('\n')
        else:
            c = a/b
            print('\n')
            print('\n{} ÷ {} = {}'.format(a,b,c))
            print('\n')
        
    
    if opcao == 4:
        c = a*b
        print('\n')
        print('\n{} x {} = {}'.format(a,b,c))
        print('\n')