estados = []

for contador in range (0,3):
    estado=[input("\n Digite a UF: "), int(input("\n Digite a população: "))]
    estados.append(estado)
total_populacao =0
for estado in estados:
    print(estado[0].upper())
    total_populacao+=estado[1]
print("Total de população: " + str(total_populacao))
print("Media de população: " + str(total_populacao/len(estados)))