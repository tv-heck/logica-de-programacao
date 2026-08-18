matricula = "2026-TI-089"

print(matricula[0:4])
print(matricula[5:7])
print(matricula[8:])

placa = input("Digite a placa do veículo (formato ABC1D23): ")

letras_iniciais = placa[0:3]
sufixo = placa[3:]

print(f"Letras iniciais da sua placa: {letras_iniciais}")
print(f"Sufixo da sua placa: {sufixo}")

print("Obrigado pelo uso do programa!")