# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Escreva um algoritmo para ler o número total de eleitores de um município, o número
# de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um
# representa em relação ao total de eleitores.

totalEleitores = int(input("Digite abaixo o número total de eleitores do município "))
votosBrancos = int(input("Quantos votaram branco? "))
votosNulos = int(input("E quantos votaram nulo? "))

votosValidos = totalEleitores - (votosBrancos+votosNulos)
porcentagemValidos = (100*votosValidos)/totalEleitores
porcentagemBrancos = (100*votosBrancos)/totalEleitores
porcentagemNulos = (100*votosNulos)/totalEleitores

print("A porcentagem de votos válidos é de", porcentagemValidos)
print("A porcentagem de votos brancos é de", porcentagemBrancos)
print("A porcentagem de votos nulos é de", porcentagemNulos)