from PyPDF2 import PdfFileReader
from pathlib import Path
import glob

with Path('0001-artigo.csv').open(mode='w', encoding='utf8') as output_file:
    for file in glob.glob("*.pdf"):
        pdf = PdfFileReader(file, strict=False)
        texto = '"' + file + '";"'
        x = range(0, 1)
        for n in x:
            page_1_object = pdf.getPage(n)
            page_1_text = page_1_object.extract_text()

            if 'chave' in page_1_text.lower():
                start = page_1_text.lower().find(page_1_text.lower()[0])
                end = page_1_text.lower().find('chave') - 10
                resumo = page_1_text[start:end].replace('\n', '')
                texto += resumo + '";"'
                start = page_1_text.lower().find('chave') - 10
                end = start + 200
                palavra_chave = page_1_text[start:end].replace('\n', '')
                texto += palavra_chave + '"'
                print('\n' + texto)
                output_file.write('\n' + texto)
                break

            if 'keywords' in page_1_text.lower():
                start = page_1_text.lower().find(page_1_text.lower()[0])
                end = page_1_text.lower().find('keywords') - 10
                resumo = page_1_text[start:end].replace('\n', '')
                texto += resumo + '";"'
                start = page_1_text.lower().find('keywords')
                end = start + 200
                palavra_chave = page_1_text[start:end].replace('\n', '')
                palavra_chave = palavra_chave.replace("‐", ' ')
                texto += palavra_chave + '"'
                print('\n' + texto)
                output_file.write('\n' + texto)
                break
