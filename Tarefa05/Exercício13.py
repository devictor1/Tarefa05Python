# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Ler um valor e escrever se é positivo, negativo ou zero.

valor = float(input("Digite um valor qualquer"))
print("O seu valor é positivo") if valor>0 else print("O valor é zero") if valor == 0 else print("O valor é negativo")