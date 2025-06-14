movieName = "The Gun"
movieDescription = """
Top Gun Maverick é um filme de aviação e aventura
muito consagrado na indústria.
"""
print(movieName.upper())  # Converte a string para maiúsculas
print(movieName.lower())  # Converte a string para minúsculas
print(movieName.capitalize())  # Converte a primeira letra para maiúscula e o restante para minúsculas
print(movieName.title())  # Converte a primeira letra de cada palavra para maiúscula
print(movieName.center(10, '-'))  # Retorna string centralizada com caracteres de preenchimento
print(movieName.find("u"))  # Retorna o índice da primeira ocorrência da substring
print(movieName.find("o"))
print(movieName.replace("Gun", "Matrix"))  # Substitui uma substring por outra
print(movieDescription.split(','))  # Divide a string em uma lista de palavras