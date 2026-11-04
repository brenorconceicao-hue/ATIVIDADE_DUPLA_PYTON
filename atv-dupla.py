import os
os.system('cls')

vetor_pratos = []
vetor_precos = []

while True:
    print('''
Código      Prato               Preço
1           Picanha             R$ 25,00
2           Lasanha             R$ 20,00
3           Strogonoff          R$ 18,00
4           Bife acebolado      R$ 15,00
5           Pão com ovo         R$ 5,00
        ''')
    opcao = int(input('Digite a opção desejada: '))

    match opcao:
        case 1:
            prato = 'Picanha'
            preco = 25
        case 2:
            prato = 'Lasanha'
            preco = 20
        case 3:
            prato = 'Strogonoff'
            preco = 18
        case 4:
            prato = 'Bife acebolado'
            preco = 15
        case 5:
            prato = 'Pão com ovo'
            preco = 5
        case _:
            print('Opção inválida. \nTente novamente... \n')

    if opcao >= 1 and opcao <= 5:
        vetor_pratos.append(prato)
        vetor_precos.append(preco)

    continuar = input('Deseja escolher outro prato? \nResponda com S ou N: ').upper()
    if continuar == 'N':
        break
    os.system('cls')

if sum(vetor_precos) == 0:
    print('\nNenhum prato selecionado.')
else:
    print('\n= PRATOS ESCOLHIDOS =')
    for i, prato in enumerate(vetor_pratos, start=1):
        print(f'{i}º prato: {prato}')
    
    print(f'\nTotal: R$ {sum(vetor_precos)}')

print('\nVolte sempre!')