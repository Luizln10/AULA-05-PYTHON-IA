def areaTriangulo(comprimento,largura):
    resultado = comprimento*largura
    return resultado
comprimento = float(input("Insira o comprimento:"))
largura = float(input("Insira a largura:"))

resultado = areaTriangulo(comprimento, largura)
print(f"Media: {resultado}")