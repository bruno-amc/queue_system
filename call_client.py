import tkinter as tk
from api_client import get_called_tickets, create_ticket, update_data, get_data

def call_next_ticket():
    data = get_data()
    for ticket in data['tickets']:
        if not ticket['called']:
            ticket['called'] = True
            update_data(data)
            current_ticket_label.config(text=f"Senha: {ticket['id']}\nTipo: {ticket['type']}\nPrioridade: {'Sim' if ticket['priority'] else 'Não'}")
            break

def call_previous_ticket():
    # Implementar lógica para chamar o ticket anterior, se necessário.
    pass

def show_last_called_tickets():
    called_tickets = get_called_tickets()
    if called_tickets:
        tickets_text = "\n".join([f"Senha: {t['id']} | Tipo: {t['type']} | Prioridade: {'Sim' if t['priority'] else 'Não'}" for t in called_tickets[-5:]])
        last_called_label.config(text=tickets_text)
    else:
        last_called_label.config(text="Nenhuma senha chamada ainda.")

window = tk.Tk()
window.title("Chamada de Senhas")

current_ticket_label = tk.Label(window, text="Nenhuma senha chamada.")
current_ticket_label.pack()

tk.Button(window, text="Chamar Próxima Senha", command=call_next_ticket).pack()
tk.Button(window, text="Exibir Últimas Senhas Chamadas", command=show_last_called_tickets).pack()

last_called_label = tk.Label(window, text="")
last_called_label.pack()

window.mainloop()
