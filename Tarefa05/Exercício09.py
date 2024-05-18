# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python

# Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que
# diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

anoAtual = int(input("Em que ano estamos?"))
anoNascimento = int(input("E em qual ano você nasceu?"))

print("Baseado apenas nos anos, você não pode votar!") if anoAtual-anoNascimento<16 else print("Baseado apenas nos anos, você pode votar esse ano!")