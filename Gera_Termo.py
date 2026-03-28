import tkinter as tk
from tkinter import messagebox, filedialog
from docx import Document
import json
from datetime import datetime
import os.path

# Arquivo de histórico
HISTORICO_FILE = 'termo_historico.json'

def obter_proximo_id():
    """Obtém o próximo ID disponível para um termo"""
    try:
        with open(HISTORICO_FILE, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            if dados['termos']:
                return max(t['id'] for t in dados['termos']) + 1
    except:
        pass
    return 1

def salvar_no_historico(modelo_l, serial_l, modelo_d, serial_d, nome, mochila):
    """Salva um termo no histórico"""
    try:
        historico = carregar_historico()
        novo_termo = {
            'id': obter_proximo_id(),
            'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'modelo_l': modelo_l,
            'serial_l': serial_l,
            'modelo_d': modelo_d,
            'serial_d': serial_d,
            'nome': nome,
            'mochila': mochila
        }
        historico['termos'].append(novo_termo)

        with open(HISTORICO_FILE, 'w', encoding='utf-8') as f:
            json.dump(historico, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Erro ao salvar histórico: {e}")

def carregar_historico():
    """Carrega o histórico de termos"""
    if os.path.exists(HISTORICO_FILE):
        try:
            with open(HISTORICO_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {'termos': []}
    return {'termos': []}

def deletar_do_historico(termo_id):
    """Deleta um termo do histórico"""
    try:
        historico = carregar_historico()
        historico['termos'] = [t for t in historico['termos'] if t['id'] != termo_id]

        with open(HISTORICO_FILE, 'w', encoding='utf-8') as f:
            json.dump(historico, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Erro ao deletar do histórico: {e}")
        return False

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

        # Salvar no histórico
        salvar_no_historico(
            dados['[Modelo_L]'],
            dados['[Laptop_Serial]'],
            dados['[Modelo_D2]'],
            dados['[Dock_Serial]'],
            dados['[Nome]'],
            dados['[check_m]']
        )

        messagebox.showinfo("Sucesso", f"O termo foi salvo com sucesso em:\n{arquivo_salvar}")

    except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo 'Modelo_termo.docx' não encontrado na pasta do programa.")
    except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")
