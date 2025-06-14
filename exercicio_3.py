#3 - Verifique se uma string fornecida é um palidromo
#(pode ser lida da mesma forma de trás para frente)

texto1 = "arara"
texto2 = "python"

#remove espaços e converte para minúsculas
texto1_format = texto1.lower().replace(" ", "")
texto2_format = texto2.lower().replace(" ", "")

#verifica se o texto é igual ao seu reverso
palindromo1 = texto1_format == texto1_format[::-1]
palindromo2 = texto2_format == texto2_format[::-1]

print(palindromo1)
print(palindromo2)
