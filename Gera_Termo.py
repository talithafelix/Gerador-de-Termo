from pydoc import doc
import tkinter as tk
from tkinter import messagebox, filedialog
from docx import Document
import os

#Função para gerar o termo
def gerar_termo(modelo_l,serial_l,modelo_d,serial_d,nome,rbtn_mochila):
    dados = {
        '[Modelo_L]': modelo_l.get(),
        '[Laptop_Serial]': serial_l.get(),
        '[Modelo_D]': modelo_d.get(),
        '[Dock_Serial]': serial_d.get(),
        '[Nome]': nome.get(),
        '[check_m]': rbtn_mochila.get(),
        '[check_d]': "(       )",
        '[Modelo_D2]':'Dockstation'

    }

    hifen = ' - '

    if dados['[Modelo_D]']:
          dados["[check_d]"] = '(  X  )'
          dados['[Modelo_D2]'] = dados['[Modelo_D]']
          dados['[Modelo_D]'] = hifen + dados['[Modelo_D]'] + hifen

    if not dados['[Modelo_L]']:
            messagebox.showerror("Erro", "Preencha o modelo do laptop!")
            return
    if not dados['[Laptop_Serial]']:
            messagebox.showerror("Erro", "Preencha o número de série do laptop!")
            return
    if  dados['[Modelo_D2]'] != 'Dockstation' and not dados['[Dock_Serial]']:
            messagebox.showerror("Erro", "Preencha o número e série da Docking Station!")
            return
    if not dados['[Nome]']:
             messagebox.showerror("Erro", "Preencha o nome do usuário!")

    nome_sugerido = f"{dados['[Nome]']}.docx"

    arquivo_salvar = filedialog.asksaveasfilename(
        defaultextension=".docx",
        initialfile=nome_sugerido,#Ja sugere salvar com o nome do usuário
        filetypes=[("Documentos do Word", ".docx"), ("Todos os arquivos", ".*")],
        title="Salvar termo como..."
    )
    if not arquivo_salvar: # Se o usuário cancelou
        return
    
    
    try:
        #Criar o Documento
        modelo_termo = Document('Modelo_termo.docx')
        #Percorrendo cada paragrafo
        for paragraph in modelo_termo.paragraphs:
            #Percorre o dicionario
            for key, value in dados.items():
                #Substitui o texto igual a chave pelo valor digitado
                for run in paragraph.runs:
                    run.text = run.text.replace(key, value)
        
        modelo_termo.save(arquivo_salvar)
        messagebox.showinfo("Sucesso", f"O termo foi salvo com sucesso em:\n{arquivo_salvar}")

    except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo 'Modelo_termo.docx' não encontrado na pasta do programa.")
    except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")
