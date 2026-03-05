def suma_1_a_n(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return n + suma_1_a_n(n - 1)


if __name__ == "__main__":
    n = int(input("Ingrese n para calcular la suma de 1 a n: "))
    print(f"Suma de 1 a {n} = {suma_1_a_n(n)}")
    