import tkinter as tk
from tkinter import messagebox, ttk
from Gera_Termo import gerar_termo, carregar_historico, deletar_do_historico

janela = tk.Tk()
janela.title('Gerador de Termo')
janela.geometry('550x650')

# Modelos pré-definidos
modelos_laptop = ["Dell", "HP", "Lenovo"]
modelos_dockstation = ["Dell", "HP", "Lenovo", "Lenovo ThinkPad"]

# ===== FUNÇÕES DE HISTÓRICO =====

def listar_historico():
    """Atualiza a listbox com o histórico de termos"""
    historico = carregar_historico()
    lista_historico.delete(0, tk.END)

    for termo in reversed(historico['termos']):  # Mais recentes primeiro
        txt = f"{termo['nome']} - {termo['data']} - {termo['modelo_l']} / {termo['modelo_d']}"
        lista_historico.insert(tk.END, txt)

def carregar_termo_selecionado():
    """Carrega um termo do histórico para os campos de edição"""
    try:
        index = lista_historico.curselection()[0]
        historico = carregar_historico()
        termo = list(reversed(historico['termos']))[index]

        # Preencher campos
        combo_modelo_l.delete(0, tk.END)
        combo_modelo_l.insert(0, termo['modelo_l'])

        entry_serial_l.delete(0, tk.END)
        entry_serial_l.insert(0, termo['serial_l'])

        combo_modelo_d.delete(0, tk.END)
        combo_modelo_d.insert(0, termo['modelo_d'])

        entry_serial_d.delete(0, tk.END)
        entry_serial_d.insert(0, termo['serial_d'])

        entry_nome.delete(0, tk.END)
        entry_nome.insert(0, termo['nome'])

        rbtn_mochila.set(termo['mochila'])

        # Ir para a aba de geração
        notebook.select(0)
        messagebox.showinfo("Sucesso", "Termo carregado! Você pode editar e gerar novamente.")
    except IndexError:
        messagebox.showerror("Erro", "Selecione um termo para carregar!")

def deletar_termo_selecionado():
    """Deleta um termo do histórico"""
    try:
        index = lista_historico.curselection()[0]
        historico = carregar_historico()
        termo = list(reversed(historico['termos']))[index]

        if messagebox.askyesno("Confirmar", f"Deletar o termo de {termo['nome']} ({termo['data']})?"):
            deletar_do_historico(termo['id'])
            listar_historico()
            messagebox.showinfo("Sucesso", "Termo deletado do histórico!")
    except IndexError:
        messagebox.showerror("Erro", "Selecione um termo para deletar!")

def atualizar_historico():
    """Atualiza a janela de histórico"""
    listar_historico()
    messagebox.showinfo("Sucesso", "Histórico atualizado!")

def gerar_e_atualizar():
    """Chama gerar_termo e depois atualiza histórico"""
    gerar_termo(combo_modelo_l, entry_serial_l, combo_modelo_d, entry_serial_d, entry_nome, rbtn_mochila)
    listar_historico()

# ===== INTERFACE COM ABAS =====

notebook = ttk.Notebook(janela)
notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# ===== ABA 1: GERAR TERMO =====
aba_gerar = ttk.Frame(notebook, padding=10)
notebook.add(aba_gerar, text="Gerar Termo")

tk.Label(aba_gerar, text="Modelo Laptop:").pack(pady=5)
combo_modelo_l = ttk.Combobox(aba_gerar, values=modelos_laptop, width=48, state="normal")
combo_modelo_l.pack()

tk.Label(aba_gerar, text="Nº Série do Laptop:").pack(pady=5)
entry_serial_l = tk.Entry(aba_gerar, width=50)
entry_serial_l.pack()

tk.Label(aba_gerar, text="Modelo DockStation:").pack(pady=5)
combo_modelo_d = ttk.Combobox(aba_gerar, values=modelos_dockstation, width=48, state="normal")
combo_modelo_d.pack()

tk.Label(aba_gerar, text="Nº Série da DockStation:").pack(pady=5)
entry_serial_d = tk.Entry(aba_gerar, width=50)
entry_serial_d.pack()

tk.Label(aba_gerar, text="Nome do Colaborador:").pack(pady=5)
entry_nome = tk.Entry(aba_gerar, width=50)
entry_nome.pack()

#Radio button Mochila
tk.Label(aba_gerar, text="Recebeu a Mochila?").pack(pady=5)
rbtn_mochila = tk.StringVar(value="(       )") # Valor padrão
frame_mochila = tk.Frame(aba_gerar)
frame_mochila.pack()
tk.Radiobutton(frame_mochila, text="Sim", variable=rbtn_mochila, value="(  X  )").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(frame_mochila, text="Não", variable=rbtn_mochila, value="(       )").pack(side=tk.LEFT, padx=10)

#Botão
tk.Button(aba_gerar, text="Gerar Termo", command=gerar_e_atualizar, bg="blue", fg="white", padx=20, pady=10).pack(pady=20)

# ===== ABA 2: HISTÓRICO =====
aba_historico = ttk.Frame(notebook, padding=10)
notebook.add(aba_historico, text="Histórico")

tk.Label(aba_historico, text="Termos Gerados:", font=("Arial", 10, "bold")).pack(pady=5)

# Scrollbar para listbox
scrollbar = ttk.Scrollbar(aba_historico)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lista_historico = tk.Listbox(aba_historico, yscrollcommand=scrollbar.set, height=15, width=65)
lista_historico.pack(fill=tk.BOTH, expand=True, pady=5)
scrollbar.config(command=lista_historico.yview)

# Frame com botões
frame_botoes = tk.Frame(aba_historico)
frame_botoes.pack(pady=10)

tk.Button(frame_botoes, text="Carregar", command=carregar_termo_selecionado, bg="green", fg="white", padx=10, pady=5).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botoes, text="Deletar", command=deletar_termo_selecionado, bg="red", fg="white", padx=10, pady=5).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botoes, text="Atualizar", command=atualizar_historico, bg="gray", fg="white", padx=10, pady=5).pack(side=tk.LEFT, padx=5)

# Carregar histórico na inicialização
listar_historico()

janela.mainloop()