import urllib.request
import urllib.error
import re
from urllib.parse import urljoin


def baixar_conteudo(url):

    requisicao = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    resposta = urllib.request.urlopen(
        requisicao,
        timeout=5
    )

    return resposta.read().decode(
        "utf-8",
        errors="ignore"
    )


def javascript_recon(url):

    print("\n[7] JAVASCRIPT RECON")
    print("-" * 60)

    try:
        html = baixar_conteudo(url)

    except (urllib.error.URLError, TimeoutError):

        print("[-] Não foi possível acessar a página.")
        return

    # Encontra arquivos JavaScript no HTML
    scripts = re.findall(
        r'<script[^>]+src=["\']([^"\']+)["\']',
        html,
        re.IGNORECASE
    )

    scripts = set(
        urljoin(url, script)
        for script in scripts
    )

    print(f"[+] JavaScripts encontrados: {len(scripts)}")

    for script in sorted(scripts):
        print(f"    {script}")

    endpoints = set()

    # Analisa cada JavaScript encontrado
    for script in sorted(scripts):

        print(f"\n[>] Analisando: {script}")

        try:
            codigo = baixar_conteudo(script)

        except (urllib.error.URLError, TimeoutError):

            print("    [-] Não foi possível acessar.")
            continue

        # fetch("/api/users")
        fetches = re.findall(
            r'fetch\(\s*["\']([^"\']+)["\']',
            codigo,
            re.IGNORECASE
        )

        for endpoint in fetches:
            endpoints.add(endpoint)

        # axios.get("/api/users")
        # axios.post("/api/login")
        # axios.put("/api/user")
        # axios.delete("/api/user")
        axios = re.findall(
            r'axios\.(get|post|put|delete)\(\s*["\']([^"\']+)["\']',
            codigo,
            re.IGNORECASE
        )

        for metodo, endpoint in axios:
            endpoints.add(
                f"{metodo.upper()} {endpoint}"
            )

        # XMLHttpRequest + open()
        xhr = re.findall(
            r'\.open\(\s*["\'](GET|POST|PUT|DELETE)["\']\s*,\s*["\']([^"\']+)["\']',
            codigo,
            re.IGNORECASE
        )

        for metodo, endpoint in xhr:
            endpoints.add(
                f"{metodo.upper()} {endpoint}"
            )

    print("\n" + "=" * 60)
    print("ENDPOINTS ENCONTRADOS")
    print("=" * 60)

    if endpoints:

        for endpoint in sorted(endpoints):
            print(f"[+] {endpoint}")

    else:

        print("[-] Nenhum endpoint identificado.")

    print(f"\n[+] Total de endpoints: {len(endpoints)}")