import socket


def informacoes_dominio(dominio):

    print("\n[1] INFORMAÇÕES DO DOMÍNIO")
    print("-" * 45)

    try:
        nome, aliases, ips = socket.gethostbyname_ex(dominio)

        print(f"Nome: {nome}")

        print("Aliases:")

        if aliases:
            for alias in aliases:
                print(f"  - {alias}")
        else:
            print("  Nenhum")

        print("IPs:")

        for ip in ips:
            print(f"  - {ip}")

    except socket.gaierror:
        print("Não foi possível resolver o domínio.")