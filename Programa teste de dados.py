import tkinter as tk
from tkinter import ttk
import random

def teste_de_sucesso(dificuldade, quantidade_dados):
    resultado_text.delete("1.0", tk.END)  # Limpar o campo de texto antes de exibir novo resultado
    resultado_text.insert(tk.END, f"\nTestando {quantidade_dados} dados:\n")
    sucesso_total = 0
    um_total = 0

    for _ in range(quantidade_dados):
        # Gerar um número aleatório entre 1 e 10 para cada dado
        tentativa = random.randint(1, 10)
        
        # Verificar se a tentativa do jogador é maior ou igual à dificuldade
        if tentativa >= dificuldade:
            sucesso_total += 1
            resultado_text.insert(tk.END, f"Número do dado lançado: {tentativa}\n")
        elif tentativa == 1:
            um_total += 1
            resultado_text.insert(tk.END, f"Número do dado lançado: {tentativa} - falha\n")
        else:
            resultado_text.insert(tk.END, f"Número do dado lançado: {tentativa}\n")

    # Exibir o total de sucessos apenas se não houver falha crítica
    resultado_text.insert(tk.END, f"Total de sucessos: {sucesso_total}\n")
    
    # Verificar se o número de falhas é maior que o número de sucessos
    if um_total > sucesso_total:
        resultado_text.insert(tk.END, f"Falha Crítica!!!\n")
    else:
        # Subtrair um sucesso para cada "1" encontrado nos dados
        sucesso_total -= um_total
        
        # Verificar se o jogador teve sucesso ou não
        if sucesso_total > 0:
            resultado_text.insert(tk.END, f"Você obteve {sucesso_total} sucessos.\n")
        else:
            resultado_text.insert(tk.END, "Você não teve sucesso.\n")

# Criar janela principal
root = tk.Tk()
root.title("Vampiro: A Máscara - Teste de Dados")

# Configurar estilo
style = ttk.Style()
style.theme_use("clam")

# Criar frame
frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Adicionar widgets
ttk.Label(frame, text="Dificuldade:").grid(column=0, row=0, sticky=tk.W)
dificuldade_var = tk.StringVar(value="1")
dificuldade_entry = ttk.Entry(frame, textvariable=dificuldade_var, width=10)
dificuldade_entry.grid(column=1, row=0)

ttk.Label(frame, text="Quantidade de Dados:").grid(column=0, row=1, sticky=tk.W)
dados_var = tk.StringVar(value="1")
dados_entry = ttk.Entry(frame, textvariable=dados_var, width=10)
dados_entry.grid(column=1, row=1)

testar_button = ttk.Button(frame, text="Testar", command=lambda: teste_de_sucesso(int(dificuldade_var.get()), int(dados_var.get())))
testar_button.grid(column=0, row=2, columnspan=2)

resultado_text = tk.Text(frame, wrap="word", width=40, height=10)
resultado_text.grid(column=0, row=3, columnspan=2)

# Ajustar espaçamento entre widgets
for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Focar no campo de entrada de dificuldade
dificuldade_entry.focus()

# Iniciar loop da aplicação
root.mainloop()