def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    num = int(input("Ingrese un número para calcular su factorial: "))
    print(f"{num}! = {factorial(num)}")