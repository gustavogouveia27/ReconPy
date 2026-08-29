import urllib.request
import urllib.error
import re


def coletar_urls(url):

    print("\n[4] URLs ENCONTRADAS")
    print("-" * 45)

    try:

        requisicao = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        resposta = urllib.request.urlopen(
            requisicao,
            timeout=5
        )

        html = resposta.read().decode(
            "utf-8",
            errors="ignore"
        )

        links = re.findall(
            r'href=["\'](.*?)["\']',
            html,
            re.IGNORECASE
        )

        if links:

            for link in links:
                print(f"[+] {link}")

        else:
            print("Nenhuma URL encontrada.")

    except (urllib.error.URLError, TimeoutError):

        print("Não foi possível acessar o site.")