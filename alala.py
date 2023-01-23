import tkinter as tk
from tkinter import ttk
import datetime as dt

outraJanela = tk.Tk()
label_descricao = tk.Label(text="Dados salvos com sucesso")
label_descricao.grid(row=1, column=0,padx = 10, pady=10, sticky='nswe', columnspan =4 )
    
outraJanela.mainloop()