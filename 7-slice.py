movieName = "Top Gun"

# string[início:fim] - indice começa na posição 0 | indice final - 1

#1 - buscar toda string a partir da primeira posição
print(movieName[0:]) 

#2 - buscar toda string até a última posição (sempre descarta a última posição)
print(movieName[:7]) 

#3 - buscar toda string da terceira até a ultima posição
print(movieName[2:])

"""
string[inicio:fim:passo] 
indice começa na posição 0 | indice final - 1 | 
passo - determina o incremento. Por padrão esse número é o 1
"""
#4 - buscar toda a string de 2 em 2 caractetres
print(movieName[::2])  # TopGun

#5 - buscar toda a string nos indices impares
print(movieName[1::2])  # o u

#6 - inverter a string de trás para frente
print(movieName[::-1])  # nuG poT