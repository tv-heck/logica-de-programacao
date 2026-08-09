# Atividade 1 - Caixa de supermercado

quantidade_items = int(input("Digite a quantidade de itens o cliente comprou:"))
faturamento_total = 0.0

for i in range(quantidade_items):
    preco_item = float(input(f"Digite o preço do item {i + 1}: "))
    faturamento_total += preco_item
    media = faturamento_total / quantidade_items

print("--- RELATÓRIO DE VENDAS ---")
print(f"Quantidade de itens vendidos: {quantidade_items}")
print(f"Faturamento total: R${faturamento_total:.2f}")
print(f"Média por item: R${media:.2f}")

# Atividade 2 - Tabela de parcelamento

total_compra = 1200.00

print('=' * 36)
print(f'TABELA DE PARCELAMENTO - COMPRA R$ {total_compra:.2f}')
print('=' * 36)

for i in range(1, 11):
    parcela = total_compra / i
    print(f'{i}x de R$ {parcela:.2f}')

print('=' * 36)

# Atividade 3 - Monitor de consumo de energia 

consumo_total = 0.0
dias_consumo_alto = 0


for i in range(1,8):
    consumo = float(input(f"Informe o seu consumo no dia {i}: "))
    if consumo > 20:
        print(f"ALERTA: Consumo alto no dia {i}!") 
        dias_consumo_alto += 1
    else:
        print(f"Consumo normal no dia {i}.")

    consumo_total += consumo

print(f"Consumo total da semana: {consumo_total:.2f} kWh")    
print(f"Dias com consumo alto: {dias_consumo_alto}")

# Atividade 4 - Contagem regressive (Sistema de segurança)

for i in range (15, -1, -1):
    print(f"{i} segundos para o servidor de dados desligar!")

print("Servidor de banco de dados desligado por inatividade. Entre novamente caso se querer usar.")    