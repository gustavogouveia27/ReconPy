import urllib.request
import urllib.error


def detectar_tecnologias(url):

    print("\n[3] TECNOLOGIAS")
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

        tecnologias = []

        if "wp-content" in html:
            tecnologias.append("WordPress")

        if "react" in html.lower():
            tecnologias.append("React")

        if "jquery" in html.lower():
            tecnologias.append("jQuery")

        if "<title" in html.lower():
            tecnologias.append("HTML")

        if tecnologias:

            for tecnologia in tecnologias:
                print(f"[+] {tecnologia}")

        else:
            print("Nenhuma tecnologia identificada.")

    except (urllib.error.URLError, TimeoutError):

        print("Não foi possível acessar o site.")