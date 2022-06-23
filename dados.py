from random import randint
import time as tm

repeat_rolling = True
while repeat_rolling:
    print("You rolled the following number using the Dice -",randint(1,6))
    print("Do you wish to roll the dice again?")
    repeat_rolling = ("y" or "yes") in input().lower()

print('Obrigado !')