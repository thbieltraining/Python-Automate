import fitz
from docx import Document


def pdf_para_word(caminho_pdf, caminho_docx):

    pdf = fitz.open(caminho_pdf)

    doc = Document()

    for pagina in pdf:

        texto = pagina.get_text()

        if texto.strip():
            doc.add_paragraph(texto)

    doc.save(caminho_docx)

    pdf.close()


caminho_pdf = r"C:\Users\Pichau\.vscode\Python Automate" r"\HR_CURRICULO_2026.pdf"

caminho_docx = (
    r"C:\Users\Pichau\.vscode\Python Automate" r"\HR_CURRICULO_2026_CONVERTIDO.docx"
)


pdf_para_word(caminho_pdf, caminho_docx)

print("✅ Conversão concluída!")
print(f"📄 Arquivo criado em:\n{caminho_docx}")
