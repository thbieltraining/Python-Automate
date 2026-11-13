import os
import shutil
import zipfile
from datetime import datetime

arquivo_zip = input("Caminho do ZIP: ").strip().strip('"')

if not os.path.isfile(arquivo_zip) or not zipfile.is_zipfile(arquivo_zip):
    print("Arquivo ZIP inválido ou não encontrado.")
    exit()

data_atual = datetime.now().strftime("%d-%m-%Y")
nome_pasta = f"EXTRAIDO BDOC {data_atual}"

diretorio = os.path.dirname(arquivo_zip)
pasta_destino = os.path.join(diretorio, nome_pasta)

os.makedirs(pasta_destino, exist_ok=True)

fila_zip = [arquivo_zip]
processados = set()
contador = 0
caminho_zip_principal = os.path.realpath(arquivo_zip)

while fila_zip:

    zip_atual = fila_zip.pop(0)
    caminho_real = os.path.realpath(zip_atual)

    if caminho_real in processados:
        continue

    processados.add(caminho_real)

    print(f"Extraindo: {os.path.basename(zip_atual)}")

    try:
        with zipfile.ZipFile(zip_atual, "r") as arquivo:

            # ZIP principal mantém sua estrutura.
            # ZIPs internos extraem tudo diretamente na pasta principal.
            for membro in arquivo.infolist():

                if membro.is_dir():
                    continue

                nome_membro = membro.filename.replace("\\", "/")

                if caminho_real == caminho_zip_principal:
                    caminho_relativo = os.path.normpath(
                        nome_membro.replace("/", os.sep)
                    )

                    if (
                        os.path.isabs(caminho_relativo)
                        or os.path.splitdrive(caminho_relativo)[0]
                        or caminho_relativo == os.pardir
                        or caminho_relativo.startswith(os.pardir + os.sep)
                    ):
                        print(f"Caminho inválido ignorado: {membro.filename}")
                        continue

                    nome_arquivo = caminho_relativo
                else:
                    nome_arquivo = os.path.basename(nome_membro)

                if not nome_arquivo or nome_arquivo == ".":
                    continue

                destino = os.path.join(pasta_destino, nome_arquivo)
                os.makedirs(os.path.dirname(destino), exist_ok=True)

                with arquivo.open(membro) as origem:
                    with open(destino, "wb") as saida:
                        shutil.copyfileobj(origem, saida)

            contador += 1

    except (zipfile.BadZipFile, OSError, RuntimeError) as erro:
        print(f"Erro: {erro}")
        continue

    # Localizar ZIPs extraídos
    for raiz, pastas, arquivos in os.walk(pasta_destino):

        for nome in arquivos:

            caminho = os.path.join(raiz, nome)

            if nome.lower().endswith(".zip"):
                if os.path.realpath(caminho) not in processados:
                    fila_zip.append(caminho)

    # Excluir ZIP interno após extração
    if zip_atual != arquivo_zip:
        try:
            os.remove(zip_atual)
        except OSError as erro:
            print(f"Não foi possível excluir o ZIP interno {zip_atual}: {erro}")

print("\nExtração concluída!")
print(f"ZIPs processados: {contador}")
print(f"Pasta: {pasta_destino}")
