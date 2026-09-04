# Atividade 1 - Calcular frete

def calcular_frete(valor_compra, peso_kg):
    frete_base = peso_kg * 5
    if valor_compra > 200:
        frete_com_desconto = frete_base - (frete_base * 0.5)
        return frete_com_desconto
    else:
        return frete_base

# Atividade 2 - Cupons e taxas
taxa_processamento = 2.00

def aplicar_cupom(valor_item, cupom_desconto):
    valor_com_desconto = valor_item - (valor_item * cupom_desconto)
    valor_final = valor_com_desconto + taxa_processamento
    return valor_final

# Atividade 3 - Parcelamento regreessivo (Regressividade)

def exibir_cronograma_regressivo(parcelas_restantes, valor_parcela):
    if parcelas_restantes == 0:
        print("Todas as parcelas foram quitadas!")
        return
    else:
        print(f"Restam {parcelas_restantes} parcelas de R${valor_parcela:.2f}")
        exibir_cronograma_regressivo(parcelas_restantes - 1, valor_parcela * 0.8)


# Extra - Testes das funções
# Teste 1 - Cálculo de frete

valor_compra = 250.00
peso_kg = 10.0
frete_calculado = calcular_frete(valor_compra, peso_kg)
print(f"Frete calculado: R${frete_calculado:.2f}")  # Saída esperada: R$25.00

# Teste 2 - Aplicação de cupom
valor_item = 100.00
cupom_desconto = 0.10  # 10% de desconto
valor_final = aplicar_cupom(valor_item, cupom_desconto)
print(f"Valor final após aplicação do cupom: R${valor_final:.2f}")  # Saída esperada: R$90.00 + taxa de R$2.00 = R$92.00

# Teste 3 - Parcelamento regressivo
parcelas_restantes = 5
valor_parcela = 100.00
print("Cronograma de Parcelamento Regressivo:")
exibir_cronograma_regressivo(parcelas_restantes, valor_parcela)