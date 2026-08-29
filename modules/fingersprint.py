import urllib.request
import urllib.error


def identificar_tecnologias_avancado(url):

    print("\n[6] FINGERPRINTING DE TECNOLOGIAS")
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

        headers = str(resposta.headers).lower()

        html = resposta.read().decode(
            "utf-8",
            errors="ignore"
        ).lower()

        conteudo = headers + "\n" + html

        tecnologias = {
            "wordpress": "WordPress",
            "wp-content": "WordPress",
            "django": "Django",
            "laravel": "Laravel",
            "react": "React",
            "vue": "Vue.js",
            "angular": "Angular",
            "jquery": "jQuery",
            "bootstrap": "Bootstrap",
            "next.js": "Next.js"
        }

        encontradas = []

        for padrao, tecnologia in tecnologias.items():

            if padrao in conteudo:

                if tecnologia not in encontradas:
                    encontradas.append(tecnologia)

        if encontradas:

            for tecnologia in encontradas:
                print(f"[+] {tecnologia}")

        else:
            print("[-] Nenhuma tecnologia identificada.")

    except (urllib.error.URLError, TimeoutError):

        print("Não foi possível realizar o fingerprint.")