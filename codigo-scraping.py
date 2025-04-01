from selenium import webdriver
import requests
import zipfile
import time

## abrindo o site no navegador webdriver
navegador = webdriver.Chrome()
navegador.get('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')
time.sleep(1)

## variáveis que usei para colocar na função
url1 = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
url2 = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"

## função para download dos pdfs
def download_pdf(url, filename):
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print("pdfs baixado com sucesso")
    else:
        print("erro para baixar os pdfs")

download_pdf(url1, "anexo_I.pdf")
download_pdf(url2, "anexo_II.pdf")

## arquivos que vai ser compactado
pdf_files = ["anexo_I.pdf", "anexo_II.pdf"]
zip_filename = "anexos.zip"

## arquivos para zip
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for file in pdf_files:
        zipf.write(file)

print(f"arquivos compactados em {zip_filename}")