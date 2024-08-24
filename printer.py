from escpos.printer import Usb
import time

VENDOR_ID = 0x0483
PRODUCT_ID = 0x5720
# Inicializando a impressora USB

try:
    p = Usb(VENDOR_ID, PRODUCT_ID, 0, out_ep=0x03)
except Exception as e:
    print(f"Erro ao conectar à impressora: {e}")
    p = None


def print_ticket(ticket_id, ticket_type, is_priority):
    if p is None:
        print("****impressora não disponível / printer not available ****")
        return
    
    try:        
        hora_atual = time.strftime("%H:%M:%S")
        priority_text = "PRIORITARIO" if is_priority else "NORMAL"
        ticket_text = (
               "---- SENHA ----\n"
            f"Senha: {ticket_id}\n"
            f"Tipo: {ticket_type}\n"
            f"Prioridade: {priority_text}\n"
            f"Hora: {hora_atual}\n"
            "----------------\n"
        )
          # Imprimindo o ticket / printing the ticket
        p.text(ticket_text)
        p.cut() #not all printers can perform the cut action

        print("Ticket impresso com sucesso.")
    
    except Exception as e:
        print(f"Erro ao imprimir o ticket: {e}")

# Exemplo de uso:
#print_ticket(1001, "Caixa", True)