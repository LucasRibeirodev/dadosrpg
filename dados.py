from random import randint
import time as tm
import sys
print("Dados Disponíveis: D3 [3], D4 [4], D6 [6], D8 [8], D10 [10], D12 [12], D20 [20], D100 [100]")
repeat_rolling = True
while repeat_rolling:
    dado1 = int(input("Escolha a quantidade de lados do seu dado: "))
    quantidade = int(input('Quantos dados quer jogar? '))

    lista_dados = [3,4,6,8,10,12,20,100]
    num = randint(1,dado1)
    resultado = num*quantidade

    for dado in lista_dados:
        if (dado1 == dado):
            print(f'A soma dos seus dados ({quantidade}) jogados é: {resultado}')
            print('Você quer jogar novamente(Y/N)?')
            repeat_rolling = ("y" or "yes") in input().lower()





print('Obrigado !')