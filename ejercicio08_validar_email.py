def email_es_valido(email: str) -> bool:
    return "@" in email


def main():
    email = input("Ingrese su dirección de email: ")
    if email_es_valido(email):
        print("La dirección de email es válida.")
    else:
        print("La dirección de email no es válida.")


if __name__ == "__main__":
    main()
    