# Instala as bibliotecas necessárias
!pip install googletrans==4.0.0-rc1
!pip install PyMuPDF
!pip install pytesseract
!apt-get install tesseract-ocr
!pip install Pillow

import fitz  # PyMuPDF
from googletrans import Translator
import pytesseract
from PIL import Image
from google.colab import files
import os

# Função para traduzir texto
def traduzir_texto(texto, idioma_destino):
    tradutor = Translator()
    resultado = tradutor.translate(texto, dest=idioma_destino)
    return resultado.text

# Função para extrair texto de um arquivo de texto
def extrair_texto_txt(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        return f.read()

# Função para extrair texto de um PDF
def extrair_texto_pdf(arquivo):
    texto = ""
    with fitz.open(arquivo) as doc:
        for pagina in doc:
            texto += pagina.get_text()
    return texto

# Função para extrair texto de uma imagem
def extrair_texto_imagem(arquivo):
    imagem = Image.open(arquivo)
    texto = pytesseract.image_to_string(imagem, lang='por')  # 'por' para português
    return texto

# Função para salvar texto em um arquivo de texto
def salvar_txt(texto, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write(texto)

# Função para salvar texto em um PDF
def salvar_pdf(texto, nome_arquivo):
    doc = fitz.open()
    pagina = doc.new_page()
    pagina.insert_text((50, 50), texto)  # Insere o texto na posição (50, 50)
    doc.save(nome_arquivo)
    doc.close()

# Recebe o arquivo do usuário
uploaded = files.upload()

# Determina o tipo de arquivo com base na extensão
arquivo_nome = next(iter(uploaded))
extensao = os.path.splitext(arquivo_nome)[1].lower()

# Lida com o arquivo dependendo da extensão
if extensao == ".txt":
    texto_para_traduzir = extrair_texto_txt(arquivo_nome)
    nome_arquivo_final = "texto_traduzido.txt"
elif extensao == ".pdf":
    texto_para_traduzir = extrair_texto_pdf(arquivo_nome)
    nome_arquivo_final = "texto_traduzido.pdf"
elif extensao in [".jpg", ".jpeg", ".png", ".bmp"]:
    texto_para_traduzir = extrair_texto_imagem(arquivo_nome)
    nome_arquivo_final = "texto_traduzido.txt"  # Salva como TXT
else:
    print("Tipo de arquivo não suportado.")
    texto_para_traduzir = ""

idioma_destino = input("Digite o código do idioma de destino (por exemplo, 'pt' para português, 'en' para inglês, 'es' para espanhol): ")

if idioma_destino in ['en', 'es', 'pt']:
    print(f"Você selecionou o idioma: {idioma_destino}")
else:
    print("Código de idioma inválido.")

# Traduz o texto se ele não estiver vazio
if texto_para_traduzir:
    texto_traduzido = traduzir_texto(texto_para_traduzir, idioma_destino)
    print(f'Texto original: {texto_para_traduzir}')
    print(f'Texto traduzido: {texto_traduzido}')

    # Salva o texto traduzido no arquivo apropriado
    if extensao == ".txt":
        salvar_txt(texto_traduzido, nome_arquivo_final)
        print(f'Texto traduzido salvo em: {nome_arquivo_final}')
    elif extensao == ".pdf":
        salvar_pdf(texto_traduzido, nome_arquivo_final)
        print(f'Texto traduzido salvo em: {nome_arquivo_final}')
    elif extensao in [".jpg", ".jpeg", ".png", ".bmp"]:
        salvar_txt(texto_traduzido, nome_arquivo_final)
        print(f'Texto traduzido salvo em: {nome_arquivo_final}')

    # Permite o download do arquivo traduzido
    files.download(nome_arquivo_final)
