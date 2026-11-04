import os
os.system('cls')

vetor_pratos = []
vetor_precos = []
total_base = sum(vetor_precos)

while True:
    print('''         == SABOR DE CASA ==
Código      Prato               Preço
1           Picanha             R$ 25,00
2           Lasanha             R$ 20,00
3           Strogonoff          R$ 18,00
4           Bife acebolado      R$ 15,00
5           Pão com ovo         R$ 5,00
6           Remover prato
7           Sair do Menu
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

        case 6:

            print('\n== REMOVER PRODUTO ==')
            nome = input('Qual prato deseja remover?: ')
            if nome in vetor_pratos:
                vetor_pratos.remove(nome)
                print('Prato excluido com sucesso!')
            else:
                print('Prato não encontrado.')

        case 7:
            print("Volte sempre")
            os.system('cls')


        case _:
            print('Opção inválida. \nTente novamente... \n')

    if opcao >= 1 and opcao <= 5:
        vetor_pratos.append(prato)
        vetor_precos.append(preco)

    continuar = input('Deseja escolher outro prato? \nResponda com S ou N: ').upper()

    if continuar == 'N':
        break
    os.system('cls')

total_base = sum(vetor_precos)

if total_base == 0:
    print('\nNenhum prato selecionado.')
else:
    print('\n= PRATOS ESCOLHIDOS =')
    for i, prato in enumerate(vetor_pratos, start=1):
        print(f'{i}º prato: {prato}')
    
    print(f'\nTotal atual: R$ {total_base:.2f}')
    

    
    pagar_opcional = input("Deseja pagar a taxa opcional de 10%? (S/N): ").upper()
    
    if pagar_opcional == "S":
        total_com_taxa = total_base * 1.10
        print(f'Taxa de 10% adicionada!')
        print(f'Total final: R$ {total_com_taxa:.2f}')
    else:
        print(f'Total final: R$ {total_base:.2f}')


print('\nVolte sempre!')