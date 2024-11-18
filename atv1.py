nota = int(input("Insira a quantidade de notas:"))
soma = 0
for i in range(nota):
    notas = int(input("Insira a nota:"))
    soma+=notas

def media(nota):
    resultado = soma/nota
    return resultado
resultado = media(nota)
print(f"Media: {resultado}")