es_positivo = lambda x: x > 0


def filtrar_positivos(numeros: list) -> list:
    return list(filter(es_positivo, numeros))


if __name__ == "__main__":
    entrada = input("Ingrese números separados por espacios: ")
    numeros = [float(x) for x in entrada.split()]
    positivos = filtrar_positivos(numeros)
    print("Números positivos:", positivos)
    