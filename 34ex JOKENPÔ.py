#34. Fazer um jogo de JOKENPÔ:

from random import randint
from time import sleep

NomeU = (input('Qual o Seu Nome ? '))

print(f"Bem Vindo {NomeU}\n")

lista = ("Pedra", "Papel", "Tesoura")

computador = randint(0,2)

perguntar = int(input('''Escolha uma opcao para se jogar: 

[0] Pedra
[1] Papel
[2] Tesoura
 
Digite sua escolha: '''))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("POOH !!")
sleep(2)

print("-="*20)
print("O computador escolheu: {}".format(lista[computador]))
print("O jogador escolheu: {}".format(lista[perguntar]))
print("-="*20)

if computador == 0:
    if perguntar == 0:
        print("EMPATE !\n")
    elif perguntar == 1:
        print("JOGADOR PERDEU !\n")
    elif perguntar == 2:
        print("VOCE PERDEU !\n")
         

elif computador == 1:
    if perguntar == 0:
        print("COMPUTADOR PERDEU !\n")
    elif perguntar == 1:
        print("  \tEMPATE !\n")
    elif perguntar == 2:
        print(f"PARABENS {NomeU} VOCE VENCEU !\n")
   
   
elif computador == 2:
    if perguntar == 0:
        print(f"PARABENS {NomeU} VOCE VENCEU !\n")
    elif perguntar == 1:
        print("VOCE PERDEU !\n")
    elif perguntar == 2:
        print("  \tEMPATE !\n")
   