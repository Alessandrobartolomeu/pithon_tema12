# Pergunta quantas notas o usuário quer digitar
quantidade = int(input("Quantas notas deseja digitar? "))

soma = 0

# Loop para ler cada nota
for i in range(quantidade):
    nota = float(input(f"Digite a nota {i+1}: "))
    soma += nota

# Cálculo da média
media = soma / quantidade

# Exibição da média formatada
print(f"Média final: {media:.2f}")

# Verificação de aprovação
if media >= 7:
    print("APROVADO!")
else:
    print("REPROVADO!")