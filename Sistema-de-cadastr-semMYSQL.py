import tkinter as tk
from tkinter import ttk
import datetime as dt


lista_tipos = ["Galão","Caixa","Saco", "Unidade" ]
lista_codigos = []

janela = tk.Tk()

def mostrar_mensagem():
    outraJanela = tk.Tk()
    
    label_descricao = tk.Label(text="Dados salvos com sucesso")
    label_descricao.grid(row=1, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )
    
    outraJanela.mainloop()

#CREATE 
def command():
   
    nome_material = entry_descricao.get()
    tipo_unidade = combobox_selecionar_tipo.get()
    quantidade = entry_quant.get() 
 
    with open('dados.txt', 'w') as arquivo:
            arquivo.write("Nome do Material: " + nome_material + "\n")
            arquivo.write("Tipo do Material: " + tipo_unidade + "\n")
            arquivo.write("Quantidade do Material: " + quantidade + "\n")
    return mostrar_mensagem()
    
    
#Título da Janela

janela.title('Ferramenta de cadastro de materiais')

label_descricao = tk.Label(text="Descrição do Material")
label_descricao.grid(row=1, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )

entry_descricao = tk.Entry()
entry_descricao.grid(row=2,column=0, padx=10, pady=10, sticky='nswe', columnspan = 4)

label_tipo_unidade = tk.Label(text="Tipo da unidade do Material")
label_tipo_unidade.grid(row=3, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )

combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(row=3, column=2, padx = 10, pady=10, sticky='nswe', columnspan = 2)

label_quant =  tk.Label(text="Quantidade na unidade de material")
label_quant.grid(row=4, column=0,padx = 10, pady=10, sticky='nswe', columnspan =2 )

entry_quant =  tk.Entry()
entry_quant.grid(row=4, column=2,padx = 10, pady=10, sticky='nswe', columnspan =2 )

botao = tk.Button(text="Criar código", command=command)
botao.grid(row=5,column=0,padx = 10, pady=10,sticky='nswe', columnspan =4)

janela.mainloop()