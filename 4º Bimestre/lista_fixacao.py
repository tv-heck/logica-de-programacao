# Atividade 1 - Sum e Max
valores = [10, 20, 30, 40]
soma = sum(valores)
maximo = max(valores)
print("Soma:", soma)
print("Máximo:", maximo)

# Atividade 2 - Comportamento de Listas 
c = 0
s = 0
for x in [5, 10, 15]:
      c = c + 1
      s = s + x
print("Contagem:", c)
print("Soma:", s)

# Atividade 3 - Desafio: Média de uma lista sem laço for
numeros = [30, 40, 70, 100, 150]
media = sum(numeros) / len(numeros)
print("Média:", media)

# Atividade 4
gastos_cantina = [12.50, 6.00, 15.00, 4.50, 20.00]
for i in range(len(gastos_cantina)):
      print(f"Dia {i+1}: R${gastos_cantina[i]}")

total_gastos = sum(gastos_cantina)
maior_gasto = max(gastos_cantina)
menor_gasto = min(gastos_cantina)
media_gastos = total_gastos / len(gastos_cantina)
print(f"Total gasto na semana: R${total_gastos}")
print(f"Média diária de gastos: R${media_gastos}")
print(f"O dia mais barato: R${menor_gasto}")
print(f"O dia mais caro: R${maior_gasto}")
