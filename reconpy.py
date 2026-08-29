from modules.dominio import informacoes_dominio
from modules.subdominios import descobrir_subdominios
from modules.tecnologias import detectar_tecnologias
from modules.urls import coletar_urls
from modules.headers import analisar_headers
from modules.fingersprint import identificar_tecnologias_avancado
from modules.javascript import javascript_recon

def scanner():

    while True:

        print(r"""
██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗██████╗ ██╗   ██╗
██╔══██╗██╔════╝██╔═══██╗██╔══██╗████╗  ██║██╔══██╗╚██╗ ██╔╝
██████╔╝█████╗  ██║   ██║██████╔╝██╔██╗ ██║██████╔╝ ╚████╔╝
██╔══██╗██╔══╝  ██║   ██║██╔═══╝ ██║╚██╗██║██╔═══╝   ╚██╔╝
██║  ██║███████╗╚██████╔╝██║     ██║ ╚████║██║        ██║
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═══╝╚═╝        ╚═╝

                 P Y T H O N   R E C O N
                       R E C O N P Y
                          v1.0

===============================================================
       [ DNS ] [ SUBDOMAINS ] [ HTTP ] [ URLS ] [ HEADERS ]
===============================================================
                  AUTHORIZED USE ONLY
===============================================================
""")

        dominio = input("Domínio: ").strip()

        if dominio.lower() == "sair":
            print("\nSaindo...")
            break

        if not dominio:
            print("\n[-] Domínio inválido.")
            continue

        url = "https://" + dominio

        informacoes_dominio(dominio)

        descobrir_subdominios(dominio)

        detectar_tecnologias(url)

        coletar_urls(url)

        analisar_headers(url)

        identificar_tecnologias_avancado(url)

        javascript_recon(url)


        print("""
==========================================
             SCAN FINALIZADO
==========================================
""")

        input("Pressione ENTER para voltar ao início...")


scanner()