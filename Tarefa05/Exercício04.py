# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste aluno.
# Considerar que a média é ponderada e que o peso das notas é 2, 3 e 5. Fórmula para o cálculo da média final é:
# mediafinal =(n1 * 2 + n2 * 3 + n3 * 5)/10

nota1 = float(input("Digite a sua primeira nota"))
nota2 = float(input("Digite a sua segunda nota"))
nota3 = float(input("Digite a sua terceira nota"))

mediaPonderada = (nota1*2 + nota2*3 + nota3*5)/10

print("A sua nota final é", mediaPonderada)