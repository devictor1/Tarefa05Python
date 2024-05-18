# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito.
# Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito).
# Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo',
# senão escrever a mensagem 'Saldo Negativo'.

conta = int(input("Qual o número da sua conta?"))
saldo = float(input("E qual o saldo atual?"))
debito = float(input("E quanto você deseja retirar?"))
credito = float(input("E quanto você deseja depositar?"))
print("O saldo atual é", saldo-debito+credito)
print("Saldo Positivo.") if saldo >= 0 else print("Saldo Negativo")