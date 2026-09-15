# AV2 - Função de RH de Empresa de Vendas

nome_vendedores = []
salario_base = 1600

def cadastrar_vendedor():
    while True:
        nome = input("Digite o nome do vendedor: ")
        nome_limpo = nome.strip()
        nome_vendedores.append(nome_limpo)
        print(f"Vendedor {nome_limpo} cadastrado com sucesso!")

        continuar = input("Deseja cadastrar outro vendedor? (s/n): ").strip().lower()
        if continuar != "s":
            break

def bater_meta(meta, vendas):
        for vendedor in nome_vendedores:
            print(f"\nVerificando meta de vendas para {vendedor}:")
            if vendas >= meta:
                bonus = salario_base * 0.10
                salario_final = salario_base + bonus
                print(f"Meta batida! Salário final com bônus: R${salario_final:.2f}")
            else:
                print(f"Meta não batida. Salário final: R${salario_base:.2f}")

def fazer_relatorio(meta, vendas):
    print("\nRelatório de Vendedores:")
    for vendedor in nome_vendedores:
        if vendas >= meta:
            bonus = salario_base * 0.10
            salario_final = salario_base + bonus
            return salario_final
        else:
            return salario_base
    print("------------------------------")
            

cadastrar_vendedor()
bater_meta(5000, 7500)