from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''=-=OPÇÕES=-=:
[-0-]=-PEDRA-=
[-1-]=-PAPEL-=
[-2-]=-TESOURA-=''')

print('-_-'*11)
jg = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(0.5)
print(f'O computador escolheu {(itens[pc])}')
print(f'O jogador escolheu {(itens[jg])}')
print('-_-'*11)

if(jg == 0) and (pc == 1):
    print("Você perdeu! :(")
elif(jg == 2) and (pc == 1):
    print("Você venceu! :)")
elif(jg == 1) and (pc == 1):
    print("Empate!")
elif(jg == 0) and (pc == 2):
    print("Você venceu! :)")
elif (jg == 0) and (pc == 0):
    print("Empate!")
elif(jg == 2) and (pc == 0):
    print("Você perdeu! :(")
elif(jg == 2) and (pc == 2):
    print("Empate!")
elif(jg == 1) and (pc == 0):
    print("Você venceu! :)")
elif(jg == 1) and (pc == 2):
    print("Você perdeu! :(")
else:
    print("Escolha novamente")
