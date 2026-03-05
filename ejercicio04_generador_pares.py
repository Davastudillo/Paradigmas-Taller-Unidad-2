def pares(n: int, m: int):
    if not (n > 0 and m > 0 and n < m):
        raise Exception("No es posible continuar con la operación")
    for i in range(n, m + 1):
        if i % 2 == 0:
            yield i


if __name__ == "__main__":
    n = int(input("Ingrese n (debe ser > 0 y < m): "))
    m = int(input("Ingrese m (debe ser > 0 y > n): "))
    try:
        print("Números pares en el rango:", list(pares(n, m)))
    except Exception as e:
        print(e)