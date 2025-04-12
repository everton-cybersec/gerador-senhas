import tkinter as tk
from tkinter import messagebox
import random
import string

def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
        usar_maiusculas = var_maiusculas.get()
        usar_minusculas = var_minusculas.get()
        usar_numeros = var_numeros.get()
        usar_simbolos = var_simbolos.get()

        if sum([usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos]) < 2 or not (usar_numeros or usar_simbolos):
            messagebox.showerror(
               title="Erro!",
               message="Por motivos de segurança, você precisa incluir com caracteres ou números ou símbolos.")
            return
        
        
        caracteres = ''
        if usar_maiusculas:
            caracteres += string.ascii_uppercase
        if usar_minusculas:
            caracteres += string.ascii_lowercase
        if usar_numeros:
            caracteres += string.digits
        if usar_simbolos:
            caracteres += string.punctuation

        if tamanho < 9:
            messagebox.showerror(
                title="Erro de tamanho!",
                message="Por motivos de segurança, selecione um tamanho maior que 8 caracteres!")
            return
        
        if not caracteres:
            messagebox.showerror(
                title="Erro!", 
                message="Selecione pelo menos um tipo de caractere.")
            return
        
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha)

    except ValueError:
        messagebox.showerror(
            title="Erro!", 
            message="Informe um número válido para o tamanho.")

# Interface
janela = tk.Tk()
janela.title("Gerador de Senhas Seguras")
janela.geometry("400x300")

tk.Label(janela, text="Tamanho da Senha:").pack()
entry_tamanho = tk.Entry(janela)
entry_tamanho.pack()

var_maiusculas = tk.BooleanVar(value=True)
var_minusculas = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=False)

tk.Checkbutton(janela, text="Incluir Letras Maiúsculas", variable=var_maiusculas).pack()
tk.Checkbutton(janela, text="Incluir Letras Minúsculas", variable=var_minusculas).pack()
tk.Checkbutton(janela, text="Incluir Números", variable=var_numeros).pack()
tk.Checkbutton(janela, text="Incluir Símbolos", variable=var_simbolos).pack()

tk.Button(janela, text="Gerar Senha", command=gerar_senha).pack(pady=10)

entry_senha = tk.Entry(janela, width=30, font=('Helvetica', 12))
entry_senha.pack(pady=5)

def copiar_senha():
    senha = entry_senha.get()
    if senha:
        janela.clipboard_clear
        janela.clipboard_append(senha)
        messagebox.showinfo(
            title="Pronto!",
            message="Senha copiada para a área de transferência!")
        
tk.Button(janela, text="Copiar senha", command=copiar_senha).pack(pady=5)

janela.mainloop()


