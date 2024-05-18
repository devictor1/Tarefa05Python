# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever
# o valor correspondente em graus Celsius (baseado na fórmula abaixo):
# C= (F - 32)*5/9
# Observação: Para testar se a sua resposta está correta saiba que 100oC = 212F

fahrenheit = float(input("Digite a temperatura em graus Fahrenheit"))
celsius = ((fahrenheit - 32)*5)/9
print("A temperatura em Celsius é",celsius)