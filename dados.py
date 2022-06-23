from random import randint
import time as tm

print("Dados Disponíveis: D3 [3], D4 [4], D6 [6], D8 [8], D10 [10], D12 [12], D20 [20], D100 [100]")
dado = int(input("Escolha a quantidade de lados do seu dado: "))
lista_dados = ['3','4','6', '8', '10', '12', '20', '100']

for dado in lista_dados:
    if dado > dado: randint(1,dados)

repeat_rolling = True
while repeat_rolling:
    print(f'Você rolou o seguinte número usando os dados: {dado}')
    print("Você quer jogar novamente?")
    repeat_rolling = ("y" or "yes") in input().lower()

print('Obrigado !')