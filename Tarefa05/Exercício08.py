# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples
# e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota
# igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

nota1 = float(input("Qual foi sua nota na primeira avaliação?"))
nota2 = float(input("E qual a nota da segunda avaliação?"))
media = (nota1+nota2)/2
print('Parabéns! Você passou com uma média de',media) if media >= 6 else print('Infelizmente você não passou com a média de',media)