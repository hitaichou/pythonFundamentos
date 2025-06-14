#2 - Inverta a ordem das palavras em uma string fornecida.
texto = "Python é muito interessante"
palavras = texto.split()  # Divide a string em uma lista de palavras
texto_invertido = ' '.join(palavras[::-1])  # Inverte a lista de palavras e junta novamente
print(texto_invertido)  # Exibe o texto com as palavras invertidas