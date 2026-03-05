def validar_dni(dni: str) -> bool:
    return dni.isdigit() and len(dni) in (7, 8)


def obtener_identificador(nombre_completo: str, dni: str) -> str:
    partes = nombre_completo.strip().split()
    primer_nombre = partes[0]
    apellido = partes[-1]
    letras_apellido = len(apellido)
    tres_digitos = dni[:3]
    return f"{primer_nombre}{letras_apellido}{tres_digitos}"


def main():
    while True:
        nombre = input("Nombre completo (vacío para terminar): ").strip()
        if nombre == "":
            break
        while True:
            dni = input("DNI (7 u 8 dígitos): ").strip()
            if validar_dni(dni):
                break
            print("DNI inválido. Debe tener 7 u 8 dígitos.")
        identificador = obtener_identificador(nombre, dni)
        print(identificador)


if __name__ == "__main__":
    main()
    