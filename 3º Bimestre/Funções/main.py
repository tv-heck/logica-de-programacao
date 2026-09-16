# AV2 - Sistema de RH de Empresa de Vendas

nomes_vendedores = ["João", "Maria", "Pedro", "Ana", "Lucas"]
nome_verificado = []


def verificar_nome(nome, vendedores):
    """Retorna o nome padronizado se ele estiver cadastrado."""
    nome_normalizado = nome.strip().casefold()
    for vendedor in vendedores:
        if vendedor.casefold() == nome_normalizado:
            return vendedor
    return None


def bater_meta(vendas, meta, salario_base):
    salario_base = 2000  # Salário base do vendedor
    if vendas >= meta:
        bonus = 0.30 * salario_base
        salario_final = salario_base + bonus
        return salario_final
    else:
        return salario_base

def main_relatorio(bater_meta, vendas, meta, salario_base, nome_verificado):
    if nome_verificado:
        print("\n--- Relatório do Trimestre ---")
        print(f"\nVendedor: {nome_verificado} ")
        print(f"Vendas realizadas: {vendas}")
        print(f"Meta de vendas: {meta}")
        salario_final = bater_meta(vendas, meta, salario_base)
        print(f"Salário final do vendedor: R${salario_final:.2f}")
        if vendas >= meta:
                print("Parabéns! Você atingiu a meta de vendas e recebeu um bônus!")
        else:
                print("Que pena. Talvez da próxima vez?")


relatorio = input("Deseja gerar o relatório do trimestre? (s/n): ")
if relatorio.lower() == 's':
    nome_verificado = verificar_nome(nome_verificado, nomes_vendedores)
    main_relatorio(bater_meta, vendas=15000, meta=10000, salario_base=2000, nome_verificado=nome_verificado)
    print("\n--- Relatório do Trimestre ---")