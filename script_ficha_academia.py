import os
import sys

# Adicionar o caminho do Conda e suas dependências
conda_env_path = r'C:\Users\Dan_n\miniconda3\envs\weasyprint-env'  # Substitua pelo caminho correto do seu ambiente Conda
os.environ['PATH'] = conda_env_path + r'\Library\bin;' + os.environ['PATH']
os.environ['PATH'] = conda_env_path + r'\Scripts;' + os.environ['PATH']
os.environ['PATH'] = conda_env_path + r'\Library\mingw-w64\bin;' + os.environ['PATH']
os.environ['PATH'] = conda_env_path + r'\Library\usr\bin;' + os.environ['PATH']
os.environ['PATH'] = conda_env_path + r'\Library\bin;' + os.environ['PATH']
os.environ['PATH'] = conda_env_path + r'\condabin;' + os.environ['PATH']

# Coletando a entrada dos dados
nome = input("Digite o nome do aluno(a): ")
idade = input("Digite a idade do aluno(a): ")
peso = input("Digite o peso do aluno(a) (Kg): ")
altura = input("Digite a altura do aluno(a) (m): ")

# Calculando o IMC e convertendo o mesmo para float porque é recebido como STR
imc = float(peso) / (float(altura) ** 2)

# Criando a condição e o status que vai printar
status = "dentro do peso"
if imc > 25:
    status = "sobrepeso"
elif imc < 16:
    status = "magreza"
else:
    status = "pesook"

# Importando a biblioteca que gera os PDFs já instaladas localmente
from pdf_reports import pug_to_html, write_report

# Criando dicionário que vai receber os dados fornecidos pelo usuário com chave e valor
dados_aluno = {
    "nome": nome,
    "idade": idade,
    "peso": peso,
    "altura": altura,
    "imc": imc,
    "status": status
}

# Use o meu template .pug que está no repositório
template = pug_to_html(r"C:\Users\Dan_n\Desktop\Curso_Expert_Python_EmpowerData\Degrau_1\Notebooks_Acompanhamento\7_Business_Case\template.pug", dados=dados_aluno)

# Importar WeasyPrint
import weasyprint

# Gerando o PDF - Ficha do Aluno
write_report(template, r"C:\Users\Dan_n\Desktop\Curso_Expert_Python_EmpowerData\Degrau_1\Notebooks_Acompanhamento\7_Business_Case\ficha_aluno.pdf", use_default_styling=False)

# Ativar no terminal o conda antes de executar:
# conda activate weasyprint-en
# comadno para rodar o script

# python "C:\Users\Dan_n\Desktop\Curso_Expert_Python_EmpowerData\Degrau_1\Notebooks_Acompanhamento\7_Business_Case\script_ficha_academia.py"
