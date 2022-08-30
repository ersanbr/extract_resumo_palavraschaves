from PyPDF2 import PdfFileReader
from pathlib import Path
import glob

with Path('0001-artigo.csv').open(mode='w', encoding='utf8') as output_file: # Cria o arquivo de armazenamento das informações
    for file in glob.glob("*.pdf"):                     # Varre o diretorio corrente em busca de artigos
        pdf = PdfFileReader(file, strict=False)                       # cria o objeto
        texto = '"' + file + '";"'                      # insere o nome do arquivo no arquivo de armazenamento
        x = range (0,1)                                 # restringe as páginas que serão alvo da consulta por resumo
        for n in x:                                     # Loop de consulta por resumo e introdução
            page_1_object = pdf.getPage(n)
            page_1_text = page_1_object.extract_text()

            """ Busca por regex
            s = page_1_text.lower().replace('\n','')
            
            #s = 'Part 1. Part 2. Part 3 then more text'
            resumo = re.search('resumo(.*)palavras chave', s)
            print (resumo.group(1))
            palavraChave = re.search('palavras chave(.*)\.', s).group(1)
            print(palavraChave)"""

            if 'resumo' in page_1_text.lower():                     # Busca por resumo dentro da página
                start = page_1_text.lower().find('resumo')          # Define o ponteiro da locação da palavra resumo
                end = page_1_text.lower().find('chave')-10             # Define o ponteiro da locação da palavra -chave
                resumo = page_1_text[start:end].replace('\n','')    # Exporta todo o conteudo entre o ponteiro de inicio e de fim
                texto += resumo + '";"'                             # Insere o conteúdo exportado na variável de tranferência
                               
            if 'chave' in page_1_text.lower():                     # Busca por -chave dentro da página
                start = page_1_text.lower().find('chave')-10          # Define o ponteiro da locação da palavra resumo
                end = page_1_text.lower().find('introdu')-2         # Define o ponteiro da locação da palavra introdu
                palavra_chave = page_1_text[start:end].replace('\n','')    # Exporta todo o conteudo entre o ponteiro de inicio e de fim
                texto += palavra_chave + '"'                               # Insere o conteúdo exportado na variável de tranferência
                print('\n' + texto)                                 # imprime na tela o conteúdo da variável de transferência
                output_file.write('\n' + texto)                     # tranfere o conteudo  coletado para o arquivo de armazenamento
                break

            if 'abstract' in page_1_text.lower():                   # Busca por resumo dentro da página
                start = page_1_text.lower().find('abstract')        # Define o ponteiro da locação da palavra abstract
                end = page_1_text.lower().find('keywords')          # Define o ponteiro da locação da palavra keywords
                resumo = page_1_text[start:end].replace('\n','')    # Exporta todo o conteudo entre o ponteiro de inicio e de fim
                #resumo = resumo.replace("’",' ')                    # Substitui a aspa simples por espaço
                resumo = resumo.replace("‐",' ')                    # Substitui a aspa simples por espaço
                texto += resumo + '";"'                             # Insere o conteúdo exportado na variável de tranferência
                
            if 'keywords' in page_1_text.lower():                   # Busca por resumo dentro da página
                start = page_1_text.lower().find('keywords')        # Define o ponteiro da locação da palavra resumo
                end = page_1_text.lower().find('introduction')-2    # Define o ponteiro da locação da palavra introduction
                palavra_chave = page_1_text[start:end].replace('\n','')    # Exporta todo o conteudo entre o ponteiro de inicio e de fim
                #palavra_chave = page_1_text[start:end].replace("'",' ')    # Substitui a aspa simples por espaço
                #palavra_chave = palavra_chave.replace("’",' ')    # Substitui a aspa simples por espaço
                palavra_chave = palavra_chave.replace("‐",' ')    # Substitui a aspa simples por espaço
                texto += palavra_chave + '"'                               # Insere o conteúdo exportado na variável de tranferência
                print('\n' + texto)                                 # imprime na tela o conteúdo da variável de transferência
                output_file.write('\n' + texto)                     # tranfere o conteudo  coletado para o arquivo de armazenamento
                break 
