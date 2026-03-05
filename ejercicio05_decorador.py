def imprimir_resultado(f):
    def funcion_decorada(*args, **kwargs):
        resultado = f(*args, **kwargs)
        print("Resultado de la operación:", resultado)
        return resultado
    return funcion_decorada


@imprimir_resultado
def sumar(a: float, b: float) -> float:
    return a + b


@imprimir_resultado
def multiplicar(a: float, b: float) -> float:
    return a * b


if __name__ == "__main__":
    sumar(3, 5)
    multiplicar(4, 7)