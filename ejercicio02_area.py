def area_rectangulo(anchura: float, altura: float) -> float:
    return anchura * altura


def main():
    anchura = float(input("Ingrese la anchura del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    resultado = area_rectangulo(anchura, altura)
    print(f"El área del rectángulo es: {resultado}")


if __name__ == "__main__":
    main()