import urllib.request
import urllib.error


def analisar_headers(url):

    print("\n[5] CABEÇALHOS HTTP")
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

        headers = resposta.headers

        for nome, valor in headers.items():
            print(f"{nome}: {valor}")

    except (urllib.error.URLError, TimeoutError):

        print("Não foi possível obter os cabeçalhos.")