# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

valor1 = float(input("Digite o primeiro valor!"))
valor2 = float(input("Agora, digite o segundo valor!"))

print("Os valores em ordem crescente são:",valor1,valor2) if valor2>valor1 else print("Os valores em ordem crescente são:",valor2,valor1)