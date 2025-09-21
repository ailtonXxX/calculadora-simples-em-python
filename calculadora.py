import tkinter as tk

# Função para adicionar números ou operadores
def adicionar_valor(valor):
    tela_var.set(tela_var.get() + str(valor))

# Função para calcular o resultado
def calcular():
    try:
        resultado = eval(tela_var.get())
        tela_var.set(str(resultado))
    except:
        tela_var.set("Erro")

# Função para limpar toda a tela
def limpar():
    tela_var.set("")

# Função para apagar apenas o último caractere
def apagar():
    tela_var.set(tela_var.get()[:-1])

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora Moderna")
janela.geometry("360x500")
janela.resizable(False, False)
janela.configure(bg="#1e1e2f")  # Fundo escuro

# Variável da tela
tela_var = tk.StringVar()

# Tela de exibição
tela = tk.Entry(
    janela, textvariable=tela_var, font=("Segoe UI", 28),
    bd=0, relief="flat", justify="right", bg="#292940", fg="#ffffff",
    insertbackground="white"
)
tela.pack(fill="both", ipadx=8, ipady=15, pady=15, padx=10)

# Frame para os botões
frame_botoes = tk.Frame(janela, bg="#1e1e2f")
frame_botoes.pack(expand=True, fill="both")

# Layout dos botões
botoes = [
    ["C", "⌫", "/", "*"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", "."]
]

# Função para cores dos botões
def cor_botao(valor):
    if valor in ["+", "-", "*", "/"]:
        return "#ff9500"  # Operadores laranja
    elif valor == "=":
        return "#34c759"  # Igual verde
    elif valor in ["C", "⌫"]:
        return "#ff3b30"  # Limpar e apagar vermelho
    else:
        return "#5050a5"  # Números azul escuro

# Criando os botões na interface
for linha in botoes:
    linha_frame = tk.Frame(frame_botoes, bg="#1e1e2f")
    linha_frame.pack(expand=True, fill="both")
    for botao in linha:
        if botao == "=":
            b = tk.Button(
                linha_frame, text=botao, font=("Segoe UI", 24),
                bg=cor_botao(botao), fg="white", bd=0,
                command=calcular
            )
        elif botao == "C":
            b = tk.Button(
                linha_frame, text=botao, font=("Segoe UI", 24),
                bg=cor_botao(botao), fg="white", bd=0,
                command=limpar
            )
        elif botao == "⌫":
            b = tk.Button(
                linha_frame, text=botao, font=("Segoe UI", 24),
                bg=cor_botao(botao), fg="white", bd=0,
                command=apagar
            )
        else:
            b = tk.Button(
                linha_frame, text=botao, font=("Segoe UI", 24),
                bg=cor_botao(botao), fg="white", bd=0,
                command=lambda val=botao: adicionar_valor(val)
            )
        b.pack(side="left", expand=True, fill="both", padx=5, pady=5)

# Rodar a aplicação
janela.mainloop()