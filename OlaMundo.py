print("ola mundo")

# operadores de associação

curso = "Curso de Python"
frutas = ["laranja", "uva","limão"]
saques = [1500, 100]

"Python" in curso

"mação" not in frutas

200 in saques

# como monstar funções


def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("retire seu dinheiro na boca do caixa.")


sacar(100)


#interpulação

nome = "wellington"
idade = 25
profissao = "analista"
linguagem = "Python"

print("Olá, me chamado %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculdo no cuirso de %s."%(nome, idade, profissao, linguagem))