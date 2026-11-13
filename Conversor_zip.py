import os
import zipfile
from collections import deque
from datetime import datetime

IDENTIFICADOR_PASTA = "ARQUIVOS"


def escolher_destino(diretorio, nome_pasta):
    resposta = input(
        "Deseja enviar os arquivos extraídos para PASTA_QUALQUER? (S/N): "
    ).strip().lower()

    if resposta == "s":
        return os.path.join(diretorio, "PASTA_QUALQUER", nome_pasta)
    if resposta == "n":
        return os.path.join(diretorio, nome_pasta)

    raise ValueError("Resposta inválida. Digite S ou N.")


def caminho_seguro(destino, nome_membro):
    """Impede que caminhos gravados pelo ZIP escapem da pasta de destino."""
    caminho = os.path.abspath(os.path.join(destino, nome_membro))
    raiz = os.path.abspath(destino)
    if os.path.commonpath((raiz, caminho)) != raiz:
        raise ValueError(f"Caminho inseguro dentro do ZIP: {nome_membro}")
    return caminho


def extrair():
    arquivo_zip = input("Caminho do ZIP: ").strip().strip('"')
    if not os.path.isfile(arquivo_zip) or not zipfile.is_zipfile(arquivo_zip):
        print("Arquivo ZIP inválido ou não encontrado.")
        return

    diretorio = os.path.dirname(os.path.abspath(arquivo_zip))
    nome_pasta = f"EXTRAIDO {IDENTIFICADOR_PASTA} {datetime.now():%d-%m-%Y}"
    try:
        pasta_destino = escolher_destino(diretorio, nome_pasta)
    except ValueError as erro:
        print(erro)
        return
    os.makedirs(pasta_destino, exist_ok=True)

    fila_zip = deque([(arquivo_zip, True)])
    processados = set()
    contador = 0

    while fila_zip:
        zip_atual, principal = fila_zip.popleft()
        caminho_real = os.path.realpath(zip_atual)
        if caminho_real in processados:
            continue
        processados.add(caminho_real)
        print(f"Extraindo: {os.path.basename(zip_atual)}")

        try:
            with zipfile.ZipFile(zip_atual, "r") as arquivo:
                for membro in arquivo.infolist():
                    if membro.is_dir():
                        continue
                    # O ZIP principal preserva pastas; ZIPs internos ficam achatados.
                    nome_saida = membro.filename if principal else os.path.basename(membro.filename)
                    if not nome_saida:
                        continue
                    destino = caminho_seguro(pasta_destino, nome_saida)
                    os.makedirs(os.path.dirname(destino), exist_ok=True)
                    with arquivo.open(membro) as origem, open(destino, "wb") as saida:
                        while bloco := origem.read(1024 * 1024):
                            saida.write(bloco)
            contador += 1
        except (zipfile.BadZipFile, OSError, ValueError) as erro:
            print(f"Erro ao processar {os.path.basename(zip_atual)}: {erro}")
            continue

        for raiz, _, arquivos in os.walk(pasta_destino):
            for nome in arquivos:
                if nome.lower().endswith(".zip"):
                    caminho = os.path.join(raiz, nome)
                    if os.path.realpath(caminho) not in processados:
                        fila_zip.append((caminho, False))

        if not principal:
            try:
                os.remove(zip_atual)
            except OSError as erro:
                print(f"Não foi possível excluir o ZIP interno: {erro}")

    print("\nExtração concluída!")
    print(f"ZIPs processados: {contador}")
    print(f"Pasta: {pasta_destino}")


if __name__ == "__main__":
    extrair()
