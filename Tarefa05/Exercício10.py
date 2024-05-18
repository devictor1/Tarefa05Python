# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

valor1 = float(input("Digite o primeiro valor!"))
valor2 = float(input("Agora, digite o segundo!"))

print('O maior número é o', valor1) if valor1>valor2 else print('O maior número é o', valor2)