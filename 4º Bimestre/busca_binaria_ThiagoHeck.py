# Busca binária

# Lista inicial de números
numeros = [5, 14, 17, 21, 24, 31, 32, 35, 41, 45, 47, 52, 55, 61, 65]

# Inicialização do contador
comparacoes = 0


# Solicitação do usuário
solicitacao = int(input("Digite o número que deseja buscar: "))

# Determinação do começo e fim da lista
inicio = 0
fim = len(numeros) - 1


# Procura pelo número solicitado usando busca binária
while inicio <= fim:
    comparacoes += 1
    meio = (inicio + fim) // 2
    # Se o número no meio for igual o solicitado, relata a posição e o número de comparações, caso contrário ajusta os limites da busca
    if numeros[meio] == solicitacao:
        print(f"Número {solicitacao} encontrado na posição {meio}.")
        print(f"Número de comparações realizadas: {comparacoes}")
        break
    elif numeros[meio] < solicitacao:
        inicio = meio + 1
    else:
        fim = meio - 1
# Se tudo falhar, determinamos que o número não existe na lista      
else:
    print(f"Número {solicitacao} não existe na lista.")
    print(f"Número de comparações realizadas: {comparacoes}")