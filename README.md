# Tradutor de Texto com Google Colab

Este script permite a tradução de textos extraídos de arquivos de texto (.txt), PDFs (.pdf) e imagens (.jpg, .jpeg, .png, .bmp) usando o Google Colab. O script utiliza bibliotecas como PyMuPDF, pytesseract e Google Translate para realizar a extração e tradução de texto.

## Pré-requisitos

Para executar este script, você precisará de um ambiente Google Colab. O Google Colab é uma plataforma que permite escrever e executar código Python em um navegador, sem a necessidade de configuração local.

## Instalação de Bibliotecas

O script instala automaticamente as bibliotecas necessárias ao ser executado. As bibliotecas incluem:

- `googletrans`: Para tradução de texto.
- `PyMuPDF`: Para manipulação de arquivos PDF.
- `pytesseract`: Para extração de texto de imagens.
- `Pillow`: Para manipulação de imagens.

## Como Usar

1. **Acesse o Google Colab**: Abra o [Google Colab](https://colab.research.google.com/).

2. **Crie um Novo Notebook**: Clique em "File" (Arquivo) > "New Notebook" (Novo Notebook).

3. **Copie o Código**: Cole o código do script no novo notebook.

4. **Execute o Código**: 
   - Clique no botão de execução da célula ou pressione `Shift + Enter`.
   - O script solicitará que você faça o upload de um arquivo. Escolha um dos seguintes formatos:
     - Arquivo de texto (.txt)
     - Arquivo PDF (.pdf)
     - Imagem (.jpg, .jpeg, .png, .bmp)

5. **Digite o Código do Idioma de Destino**: Após o upload do arquivo, você será solicitado a digitar o código do idioma de destino para a tradução. Os códigos válidos são:
   - `pt` para Português
   - `en` para Inglês
   - `es` para Espanhol

6. **Receba o Arquivo Traduzido**: Após a tradução, o arquivo traduzido será salvo e você poderá fazer o download dele.

## Observações

- **Limitações**: A qualidade da tradução pode variar dependendo do texto e do idioma de origem e destino.
- **Conexão com a Internet**: Certifique-se de que você está conectado à internet, pois o script utiliza serviços online para tradução e extração de texto.

## Contribuições

Sinta-se à vontade para contribuir com melhorias ou sugestões para este projeto.
