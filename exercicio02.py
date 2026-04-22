nomes = []

# Repetir 5 vezes
for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

# Exibir em maiúsculo
print("Nomes em maiúsculo:")
for nome in nomes:
    print(nome.upper())