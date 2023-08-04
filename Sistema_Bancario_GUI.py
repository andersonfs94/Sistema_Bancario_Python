import tkinter as tk

# Cria a janela
janela = tk.Tk()
janela.geometry("700x350") # Define o tamanho da janela
janela.title("Sistema Bancário")

def janela_deposito():

    janela_dep = tk.Tk()
    janela_dep.title("Depósito")
    janela_dep.geometry("550x350")
    janela_dep.config(bg="skyblue")

    caixa_texto_dep = tk.Entry(janela_dep)
    caixa_texto_dep.grid(column=0, row=0, columnspan = 3, pady=15)
    # caixa_texto_dep.place(relx=0.5)

    botao1 = tk.Button(janela_dep, text="1")
    botao1.config(command=lambda: caixa_texto_dep.insert(tk.END, "1"))
    botao1.grid(column=0, row=1)

    botao2 = tk.Button(janela_dep, text="2")
    botao2.config(command=lambda: caixa_texto_dep.insert(tk.END, "2"))
    botao2.grid(column=1, row=1)

    botao3 = tk.Button(janela_dep, text="3")
    botao3.config(command=lambda: caixa_texto_dep.insert(tk.END, "3"))
    botao3.grid(column=2, row=1)

    botao4 = tk.Button(janela_dep, text="4")
    botao4.config(command=lambda: caixa_texto_dep.insert(tk.END, "4"))
    botao4.grid(column=0, row=2)
    
    botao5 = tk.Button(janela_dep, text="5")
    botao5.config(command=lambda: caixa_texto_dep.insert(tk.END, "5"))
    botao5.grid(column=1, row=2)

    botao6 = tk.Button(janela_dep, text="6")
    botao6.config(command=lambda: caixa_texto_dep.insert(tk.END, "6"))
    botao6.grid(column=2, row=2)

    botao7 = tk.Button(janela_dep, text="7")
    botao7.config(command=lambda: caixa_texto_dep.insert(tk.END, "7"))
    botao7.grid(column=0, row=3)

    botao8 = tk.Button(janela_dep, text="8")
    botao8.config(command=lambda: caixa_texto_dep.insert(tk.END, "8"))
    botao8.grid(column=1, row=3)

    botao9 = tk.Button(janela_dep, text="9")
    botao9.config(command=lambda: caixa_texto_dep.insert(tk.END, "9"))
    botao9.grid(column=2, row=3)

    botao0 = tk.Button(janela_dep, text="0")
    botao0.config(command=lambda: caixa_texto_dep.insert(tk.END, "0"))
    botao0.grid(column=1, row=4)
    
    botao_limpa = tk.Button(janela_dep, text="Limpa")                                    
    botao_limpa.config(command=lambda: caixa_texto_dep.delete(0, tk.END))
    botao_limpa.grid(column=1, row=5, pady=5)

    botao_fechar = tk.Button(janela_dep, text="Fechar", command=janela_dep.destroy) 
    botao_fechar.grid(column=0, row=5, pady=5)                  
    
    botao_confirma = tk.Button(janela_dep, text="Confirmar")
    botao_confirma.grid(column=2, row=5, pady=5)

    janela_dep.mainloop()

# Cria a label
boasvindas = tk.Label(text="Bem-Vindo!")
boasvindas.pack()

deposito = tk.Button(text="Depósito", command=janela_deposito)
deposito.pack(padx=10, pady=10)

saque = tk.Button(text="Saque")
saque.pack(padx=10, pady=10)

extrato = tk.Button(text="Extrato")
extrato.pack(padx=10, pady=10)

#Cria um botão
botao_fechar = tk.Button(text="Fechar", command=janela.destroy)
botao_fechar.pack(padx=10, pady=80)

# Mostra a janela
janela.mainloop()