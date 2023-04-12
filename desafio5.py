'''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''


string = input("Digite uma string: ")

# Inverte a string
string_invertida = ""
for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

print("A string invertida é:", string_invertida)
