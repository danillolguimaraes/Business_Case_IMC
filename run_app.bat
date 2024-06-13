@echo off
echo Ativando o ambiente Conda...
call C:\Users\Dan_n\anaconda3\Scripts\activate.bat weasyprint-env
if errorlevel 1 (
    echo Falha ao ativar o ambiente Conda. Certifique-se de que o Anaconda está instalado corretamente.
    exit /b 1
)
echo Ambiente Conda ativado com sucesso.
echo Executando o script Python...
start "" pythonw.exe "C:\Users\Dan_n\Desktop\Curso_Expert_Python_EmpowerData\Degrau_1\Notebooks_Acompanhamento\7_Business_Case\app.pyw"
if errorlevel 1 (
    echo Falha ao executar o script Python.
    exit /b 1
)
