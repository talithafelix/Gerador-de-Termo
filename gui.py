import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
from Gera_Termo import gerar_termo

janela = tk.Tk()
janela.title('Gerador de Termo')
janela.geometry('450x450')

#Labels e Entradas

tk.Label(janela, text="Modelo Laptop:").pack(pady=5)
entry_modelo_l = tk.Entry(janela, width=50)
entry_modelo_l.pack()

tk.Label(janela, text="Nº Série do Laptop:").pack(pady=5)
entry_serial_l = tk.Entry(janela, width=50)
entry_serial_l.pack()

tk.Label(janela, text="Modelo DockStation:").pack(pady=5)
entry_modelo_d = tk.Entry(janela, width=50)
entry_modelo_d.pack()

tk.Label(janela, text="Nº Série da DockStation:").pack(pady=5)
entry_serial_d = tk.Entry(janela, width=50)
entry_serial_d.pack()

tk.Label(janela, text="Nome do Colaborador:").pack(pady=5)
entry_nome = tk.Entry(janela, width=50)
entry_nome.pack()

#Radio button Mochila

tk.Label(janela, text="Recebeu a Mochila?").pack(pady=5)
rbtn_mochila = tk.StringVar(value="(       )") # Valor padrão
frame_mochila = tk.Frame(janela)
frame_mochila.pack()
tk.Radiobutton(frame_mochila, text="Sim", variable=rbtn_mochila, value="(  X  )").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(frame_mochila, text="Não", variable=rbtn_mochila, value="(       )").pack(side=tk.LEFT, padx=10)


#Botão
btn_gerar = tk.Button(janela, text="Gerar Termo",command=lambda: gerar_termo(entry_modelo_l,entry_serial_l,entry_modelo_d,entry_serial_d,entry_nome,rbtn_mochila),bg="blue", fg="white", padx=20,pady=10).pack(pady=20)

janela.mainloop()