import tkinter as tk
from api_client import create_ticket
from printer import print_ticket

def generate_ticket():
    ticket_type = ticket_type_var.get()
    is_priority = priority_var.get() == 1  # verifica se o valor retornado por priority_var.get() é igual a 1. (true ou false)
    ticket = create_ticket(ticket_type, is_priority)
    print_ticket(ticket['id'], ticket['type'], ticket['priority'])

window = tk.Tk()
window.title("Emissão de senhas / Tickets generator")

ticket_type_var = tk.StringVar(value="Caixa")
priority_var = tk.IntVar(value=0)

tk.Label(window, text="Escolha o tipo de atendimento:").pack()
tk.Radiobutton(window, text="Caixa", variable=ticket_type_var, value="Caixa").pack()
tk.Radiobutton(window, text="Gerente", variable=ticket_type_var, value="Gerente").pack()

tk.Checkbutton(window, text="Prioridade", variable=priority_var).pack()
tk.Button(window, text="Emitir Senha", command=generate_ticket).pack()

window.mainloop()

