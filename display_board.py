import tkinter as tk
from api_client import get_called_tickets, get_data

last_ticket_count = 0  # Variável para acompanhar o número de tickets

def refresh_display():
    global last_ticket_count
    data = get_data()
    
    # Verifica se há novos tickets
    if len(data['tickets']) != last_ticket_count:
        last_ticket_count = len(data['tickets'])
        
        # Obtém as últimas senhas chamadas
        called_tickets = get_called_tickets()
        if called_tickets:
            current_ticket = called_tickets[-1]
            current_ticket_label.config(text=f"Senha Atual: {current_ticket['id']}\nTipo: {current_ticket['type']}\nPrioridade: {'Sim' if current_ticket['priority'] else 'Não'}")
            
            last_tickets = called_tickets[-5:]
            last_tickets_text = "\n".join([f"Senha: {t['id']} | Tipo: {t['type']} | Prioridade: {'Sim' if t['priority'] else 'Não'}" for t in last_tickets])
            last_called_label.config(text=last_tickets_text)
        else:
            current_ticket_label.config(text="Nenhuma senha chamada ainda.")
            last_called_label.config(text="")
    
    # Atualiza a cada 20 segundos
    window.after(20000, refresh_display)

# Configuração da interface
window = tk.Tk()
window.title("Display de Senhas Chamadas")

current_ticket_label = tk.Label(window, text="Nenhuma senha chamada.")
current_ticket_label.pack()

last_called_label = tk.Label(window, text="")
last_called_label.pack()

# Inicia o ciclo de atualização
refresh_display()

window.mainloop()
