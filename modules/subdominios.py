import socket


def descobrir_subdominios(dominio):

    print("\n[2] DESCOBRINDO SUBDOMÍNIOS")
    print("-" * 45)

    lista = [
        "www",
        "api",
        "mail",
        "blog",
        "dev",
        "test",
        "admin",
        "shop"
    ]

    encontrados = []

    for sub in lista:

        alvo = f"{sub}.{dominio}"

        try:
            ip = socket.gethostbyname(alvo)

            print(f"[+] {alvo} -> {ip}")

            encontrados.append(alvo)

        except socket.gaierror:
            pass

    print(f"\nTotal encontrados: {len(encontrados)}")