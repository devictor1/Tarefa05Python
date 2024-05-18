# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.

valor1 = float(input("Digite o primeiro valor"))
valor2 = float(input("Digite o segundo valor"))
valor3 = float(input("Digite o terceiro valor"))

print("O maior é o", valor1) if valor1>valor2 and valor1>valor3 else print("O maior é o", valor2) if valor2>valor1 and valor2>valor3 else print("O maior é o", valor3)