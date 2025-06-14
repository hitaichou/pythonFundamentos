movieName = "Top Gun"
movieName2 = "top Gun"

print(movieName == movieName2)  # False, case-sensitive comparison
print(movieName.lower() == movieName2.lower())  # True, case-insensitive comparison

movieDescription = """
Top Gun Maverick é um filme de aviação e aventura 
muito consagrado na indústria.
"""
print(movieName)
#1 - Multiplicação de strings
line = "=" * 30
print(line)
#print("================================")
print(movieDescription)

# 2 - Procurar palavra dentro de uma string
print("top" in movieName)
print("ação" in movieName)
print("muito" in movieDescription)