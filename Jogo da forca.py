from random import choice


lista_de_palavras = ['Entrevista','Desporto','Fantasia','Brincadeira','Susto','Saltitar','Desenvolvimento']

print('~' * 40)
print('JOGO DA FORCA'.center(40,'~'))
print('~' * 40)

palavra = choice(lista_de_palavras).upper().split('')


palavra_acertada = []

for letra in palavra:
    palavra_acertada.append('_')

print('PALAVRA:')
for letra in palavra_acertada:
    print(f'\033[32m{letra}\033[m ', end='')
print()
erro = len(palavra_acertada) // 2
acerto = False

while True:
    print('~' * 40)
    print(f'Voce só pode errar {erro} vez(es)...')
    chute = str(input('Digite uma letra para a palavra: ')).strip().upper()
    if chute in palavra and chute not in palavra_acertada:
        print('Acertou...')
        for pos, letra in enumerate(palavra):
            if letra == chute:
                for espaco in palavra_acertada:
                    palavra_acertada[pos] = chute           
    else:
        erro -= 1
        print('Errou...')
        
    for letra in palavra_acertada:
        print(f'\033[32m{letra}\033[m ', end='')
    print()

    if '_'  not in palavra_acertada:
        acerto = True
        print('~' * 40)
        print('Vece Ganhou...')
        print(palavra)
        break
    if erro == 0:
        print('~' * 40)
        print('Voce perdeu...')
        print(palavra)
        break
