from PyPDF2 import PdfReader


def extract_text(file_path):

    text = ""

    reader = PdfReader(file_path)

    for page in reader.pages:
        text += page.extract_text()

    return text