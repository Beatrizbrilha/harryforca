from dicionarios.dicionarios import animais, casas, personagens
from random import randint


print('\033[1;30;43m \U0001F9D9 Você é fã de harry potter? Vamos ver se consegue advinhar as palavras nesse jogo da forca! \33[m')
acertos = 0

while True:
    nome = input('Escolha um tema, Personagens, casas ou animais? ')
    if nome.lower() == 'personagens' or nome.lower() == 'casas' or nome.lower() == 'animais':
        break
    else:
        print('Escolha inválida, escolha uma das opções(personagens, casas, animais)')

palavra = ""

if nome.lower() == 'personagens':
    palavra = personagens[randint(0, len(personagens) - 1)]
elif nome.lower() == 'casas':
    palavra = casas[randint(0, len(casas) - 1)]
else:
    palavra = animais[randint(0, len(animais) - 1)]

print("A palavra selecionada tem", len(palavra), "letras.")

tentativas = len(set(palavra.lower())) + 2 # para ficar justo as tentativas

palavra_mostrada = ['_'] * len(palavra)
letras_corretas = []
letras_incorretas = []

while tentativas > 0:
    palpite = input('Chute uma letra: ')
    if palpite.lower() in palavra.lower():
        acertos += 1
        letras_corretas.append(palpite)
        for i in range(len(palavra)):
            if palavra[i].lower() == palpite.lower():
                palavra_mostrada[i] = palpite
        print("Palavra mostrada", ''.join(palavra_mostrada))
    else:
        letras_incorretas.append(palpite)
        print(f' A letra {palpite} não está presente na palavra')

    tentativas -= 1

    if acertos == len(set(palavra.lower())):
            break
print("\n Fim do jogo")

if acertos == len(set(palavra.lower())):
    print('\U0001F9D0 Parabéns! Você é bruxo(a)')
else:
    print('\U0001F615 Hmm, eu acho que você é trouxa! ')

print("A Palavra era:", palavra)