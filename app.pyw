import os
import tkinter as tk
from tkinter import messagebox
from pdf_reports import pug_to_html, write_report
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Definir o caminho do ambiente Conda e suas dependências
conda_env_path = r'C:\Users\Dan_n\anaconda3\envs\weasyprint-env'
os.environ['PATH'] = conda_env_path + r'\Library\bin;' + os.environ['PATH']
os.environ['PATH'] = conda_env_path + r'\Scripts;' + os.environ['PATH']
os.environ['PATH'] = conda_env_path + r'\Library\mingw-w64\bin;' + os.environ['PATH']
os.environ['PATH'] = conda_env_path + r'\Library\usr\bin;' + os.environ['PATH']
os.environ['PATH'] = conda_env_path + r'\Library\bin;' + os.environ['PATH']
os.environ['PATH'] = conda_env_path + r'\condabin;' + os.environ['PATH']

# Adicionar caminhos específicos do gobject e fontconfig
os.environ['GI_TYPELIB_PATH'] = conda_env_path + r'\Library\lib\girepository-1.0'
os.environ['LD_LIBRARY_PATH'] = conda_env_path + r'\Library\bin'
os.environ['FONTCONFIG_PATH'] = os.path.join(conda_env_path, 'Library', 'etc', 'fonts')

# Função para calcular o IMC e gerar o PDF
def gerar_pdf():
    nome = entry_nome.get()
    idade = entry_idade.get()
    peso = entry_peso.get()
    altura = entry_altura.get()

    try:
        imc = round(float(peso) / (float(altura) ** 2),2)
    except ValueError:
        messagebox.showerror("Erro de valor", "Por favor, insira valores numéricos válidos para peso e altura.")
        return

    if imc > 25:
        status = "Seu peso está acima do normal"
    elif imc < 18.5:
        status = "Seu peso está abaixo do normal"
    else:
        status = "Seu peso está normal"

    dados_aluno = {
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "imc": imc,
        "status": status
    }

    # Criar diretório "pdfs" se não existir
    pdf_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pdfs')
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)

    template_path = r"C:\Users\Dan_n\Desktop\Curso_Expert_Python_EmpowerData\Degrau_1\Notebooks_Acompanhamento\7_Business_Case\template.pug"
    output_path = os.path.join(pdf_dir, f"Ficha_Aluno_{nome}.pdf")

    try:
        template = pug_to_html(template_path, dados=dados_aluno)
        write_report(template, output_path, use_default_styling=False)
        messagebox.showinfo("Sucesso", f"PDF gerado com sucesso em {output_path}!")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao gerar PDF: {e}")

# Configuração da interface Tkinter
root = tk.Tk()
root.title("Calculadora de IMC")

# Estilização da interface
root.configure(bg="#f0f0f0")

# Adicionar o logo ao início do programa
try:
    logo_url = "https://lgmsolucoes.com/wp-content/uploads/2024/05/branding-lgm.png"
    response = requests.get(logo_url)
    logo_image = Image.open(BytesIO(response.content))
    logo_image = logo_image.resize((150, 75), Image.ANTIALIAS)  # Redimensionar para 150x75
    logo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(root, image=logo, bg="#f0f0f0")
    logo_label.grid(row=0, column=0, columnspan=2, pady=10)
except Exception as e:
    print(f"Erro ao carregar o logo: {e}")

tk.Label(root, text="Nome:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_nome = tk.Entry(root, width=30)
entry_nome.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Idade:", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_idade = tk.Entry(root, width=30)
entry_idade.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Peso (Kg):", bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=10, sticky="e")
entry_peso = tk.Entry(root, width=30)
entry_peso.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Altura (m):", bg="#f0f0f0").grid(row=4, column=0, padx=10, pady=10, sticky="e")
entry_altura = tk.Entry(root, width=30)
entry_altura.grid(row=4, column=1, padx=10, pady=10)

btn_gerar = tk.Button(root, text="Gerar PDF", command=gerar_pdf, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
btn_gerar.grid(row=5, column=0, columnspan=2, pady=20)

# Adicionando etiqueta "Desenvolvido por: Danillo Guimarães" em duas linhas
tk.Label(root, text="Desenvolvido por:", bg="#f0f0f0", font=("Helvetica", 10)).grid(row=6, column=0, columnspan=2)
tk.Label(root, text="Danillo Guimarães", bg="#f0f0f0", font=("Helvetica", 10, "bold")).grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()
