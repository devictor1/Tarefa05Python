# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Escreva um algoritmo para ler o salário mensal atual de um funcionário e o
# percentual de reajuste. Calcular e escrever o valor do novo salário.

salario = float(input("Digite o seu salário mensal"))
reajustePorCento = float(input("E qual o percentual de reajuste?"))

reajuste = salario*(reajustePorCento/100)
salarioNovo = salario+reajuste

print("O seu salário reajustado é", salarioNovo)