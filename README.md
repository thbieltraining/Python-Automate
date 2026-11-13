# Python Automate 🐍

Coleção de automações em Python criadas durante meus estudos, com ferramentas para arquivos ZIP, currículos, PDFs e controle do mouse/teclado.

## 📚 Projetos

| Projeto | O que faz | Como executar |
| --- | --- | --- |
| `Conversor_zip.py` | Extrai um ZIP e processa os ZIPs internos. Preserva as pastas do arquivo principal, reúne os arquivos internos na pasta de saída e permite escolher `PASTA_QUALQUER` ou a pasta ao lado do ZIP. O identificador da pasta é configurado em `IDENTIFICADOR_PASTA`. | `python Conversor_zip.py` |
| `Otimizadores para Curriculos/Tradutor_de_Curriculo.py` | Traduz parágrafos e tabelas de um currículo do português para o inglês, dividindo textos longos em blocos. | Configure os caminhos no código e execute `python "Otimizadores para Curriculos/Tradutor_de_Curriculo.py"` |
| `Otimizadores para Curriculos/Conversor_pdf_word.py` | Extrai texto de um PDF e cria um documento Word com o texto encontrado. | Configure os caminhos no código e execute `python "Otimizadores para Curriculos/Conversor_pdf_word.py"` |
| `Autoclicks Diversos/AUTOCLICK` | Aciona repetidamente a tecla `E` na janela ativa. `Espaço` inicia, `Esc` para e `Tab` encerra o programa. | `python "Autoclicks Diversos/AUTOCLICK"` |
| `Autoclicks Diversos/RASTREAR_COORDENADAS.py` | Mostra as coordenadas atuais do mouse sempre que sua posição muda. `Esc` encerra. | `python "Autoclicks Diversos/RASTREAR_COORDENADAS.py"` |
| `Autoclicks Diversos/BUSCAR_COORDENADA` | Recebe coordenadas X e Y e move o mouse até esse ponto. `Ctrl+C` encerra. | `python "Autoclicks Diversos/BUSCAR_COORDENADA"` |

## ⚙️ Requisitos

Use Python 3.10 ou superior. O extrator de ZIP usa apenas a biblioteca padrão. Para as demais ferramentas, instale as dependências:

```bash
python -m pip install python-docx deep-translator pymupdf keyboard pydirectinput pyautogui
```

## 🚀 Uso

Clone ou baixe este repositório e execute o script desejado a partir do terminal. Para caminhos que contenham espaços, mantenha o nome do arquivo entre aspas.

Os scripts de currículo têm os caminhos de entrada e saída definidos nas variáveis no início ou no corpo do arquivo. Atualize esses caminhos para os documentos que deseja processar antes de executar.

## 📝 Observações

- O tradutor usa o serviço MyMemory pela internet. O conteúdo enviado para tradução é compartilhado com esse serviço; não use documentos confidenciais sem avaliar essa divulgação.
- A conversão de PDF para Word recupera texto selecionável e não reproduz o layout original. PDFs digitalizados como imagem podem exigir OCR, que não está incluído.
- O extrator apaga cada ZIP interno depois de processá-lo. Mantenha uma cópia dos arquivos originais se precisar preservá-los.
- O autoclick usa atalhos globais de teclado e entrada simulada. Alguns jogos ou aplicativos podem exigir privilégios elevados para que os comandos sejam reconhecidos.
- Os utilitários de coordenadas usam `pyautogui` para ler ou mover o mouse. Confira a posição antes de automatizar ações em outra janela.
- Confira os caminhos de entrada e saída antes de executar os scripts para evitar processar ou substituir o arquivo errado.
