def decodificar():
    numero_decodificar = str(input('Digite um número para decodificar: '))
    lista = []
    contador = 0
    expoente = 0
    soma = 0
    for i in numero_decodificar:
        lista.insert(contador, i)
        contador += 1
    lista.reverse()
    for i in lista:
        valor_decimal_item = int(i) * (2**expoente)
        soma += valor_decimal_item
        expoente +=1
    print(soma)


def codificar():
    numero_codificar = int(input('Digite o valor para codificar: '))
    lista = []
    contador = 0
    if numero_codificar == 0:
        lista.insert(0, numero_codificar)
    else:
        while numero_codificar != 1:
            x = numero_codificar%2
            lista.insert(contador, x)
            contador +=1
            numero_codificar //= 2
        if numero_codificar == 1:
            lista.insert(contador, numero_codificar)
    lista.reverse()
    print(*lista, sep='')


print(
    '''
    ========================
    Digite a funcão desejada:
    1) Codificar
    2) Decodificar
    3) Sair
    ========================''')
escolha = int(input())

while escolha != 3:
    if escolha == 1:
        codificar()
        print(
        '''
        ========================
        Digite a funcão desejada:
        1) Codificar
        2) Decodificar
        3) Sair
        ========================''')
        escolha = int(input())
    elif escolha == 2:
        decodificar()
        print(
        '''
        ========================
        Digite a funcão desejada:
        1) Codificar
        2) Decodificar
        3) Sair
        ========================''')
        escolha = int(input())
    else:
        print('Opção inválida')
        print(
        '''
        ========================
        Digite a funcão desejada:
        1) Codificar
        2) Decodificar
        3) Sair
        ========================''')
        escolha = int(input())