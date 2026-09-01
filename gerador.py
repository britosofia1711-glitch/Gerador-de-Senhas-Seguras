import random
import string
import tkinter as tk
from tkinter import messagebox

def avaliar_forca(tamanho, tem_simbolos):
    if tamanho >= 12 and tem_simbolos:
        return "FORTE 🟢", "green"
    elif tamanho >= 8:
        return "MÉDIA 🟡", "orange"
    else:
        return "FRACA 🔴", "red"

def acao_gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
        if tamanho <= 0:
            messagebox.showwarning("Aviso", "Digite um número maior que zero!")
            return
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número válido.")
        return

    usar_simbolos = var_simbolos.get()
    
    caracteres = string.ascii_letters + string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    
    entry_resultado.delete(0, tk.END)
    entry_resultado.insert(0, senha)

    texto_forca, cor = avaliar_forca(tamanho, usar_simbolos)
    label_forca.config(text=f"Força: {texto_forca}", fg=cor)

def acao_salvar_senha():
    senha = entry_resultado.get()
    servico = entry_servico.get().strip()

    if not senha:
        messagebox.showwarning("Aviso", "Gere uma senha primeiro!")
        return
    
    if not servico:
        messagebox.showwarning("Aviso", "Digite para qual serviço é essa senha (ex: Email, Netflix)!")
        return

    with open("minhas_senhas.txt", "a") as arquivo:
        arquivo.write(f"Serviço: {servico} | Senha: {senha}\n")

    messagebox.showinfo("Sucesso", f"Senha do serviço '{servico}' salva com sucesso em 'minhas_senhas.txt'!")
    entry_servico.delete(0, tk.END)

janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("380x420")
janela.config(padx=20, pady=15)

lbl_titulo = tk.Label(janela, text="Gerador de Senhas", font=("Arial", 14, "bold"))
lbl_titulo.pack(pady=5)

lbl_tamanho = tk.Label(janela, text="Tamanho da senha:")
lbl_tamanho.pack()
entry_tamanho = tk.Entry(janela, width=10, justify="center")
entry_tamanho.insert(0, "12")
entry_tamanho.pack(pady=5)

var_simbolos = tk.BooleanVar(value=True)
chk_simbolos = tk.Checkbutton(janela, text="Incluir Símbolos (@, #, $)", variable=var_simbolos)
chk_simbolos.pack(pady=5)

btn_gerar = tk.Button(janela, text="GERAR SENHA", command=acao_gerar_senha, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_gerar.pack(pady=10)

entry_resultado = tk.Entry(janela, font=("Arial", 12), justify="center", width=25)
entry_resultado.pack(pady=5)

label_forca = tk.Label(janela, text="Força: -", font=("Arial", 10, "bold"))
label_forca.pack(pady=5)

tk.Frame(janela, height=2, bd=1, relief="sunken").pack(fill="x", pady=10)

lbl_servico = tk.Label(janela, text="Serviço (ex: Instagram, Email):")
lbl_servico.pack()
entry_servico = tk.Entry(janela, width=25)
entry_servico.pack(pady=5)

btn_salvar = tk.Button(janela, text="💾 Salvar em .txt", command=acao_salvar_senha, bg="#2196F3", fg="white", font=("Arial", 9, "bold"))
btn_salvar.pack(pady=5)

janela.mainloop()


