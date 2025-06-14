#1 - escreva um programa que le dois nomes e retorne uma string
#formatada no formato "ÚltimoNome, PrimeiroNome".

primeiroNome = input("Digite o primeiro nome: ")
segundoNome = input("Digite o segundo nome: ")

nomeFormatado = f"{segundoNome}, {primeiroNome}"

print(f"Nome formatado: {nomeFormatado}")