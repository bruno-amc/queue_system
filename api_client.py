import requests

API_URL = "WWW.XXXXX.COM...." #PRECISA???
#TODO

API_KEY = '$2a$10$JBsZiwwh5qR1neBl1nd/V./w7pXFNZJPLGVJbJqwFMOTPzHE5BGmW'

BIN_ID = '66ca2262e41b4d34e424b0b9'
BASE_URL = f"https://api.jsonbin.io/v3/b/{BIN_ID}"

HEADERS = {
    'X-Access-Key': API_KEY,
    'Content-Type': 'application/json'
}

def get_data():
    response = requests.get(BASE_URL, headers=HEADERS)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    if response.status_code == 200:
        # Extraímos o JSON até que cheguemos no nível correto
        data = response.json()['record']
        while isinstance(data, dict) and 'record' in data:
            data = data['record']
        
        # Verifica se as chaves 'last_ticket_id' e 'tickets' existem, caso contrário, as inicializa
        if 'last_ticket_id' not in data:
            data['last_ticket_id'] = 0
        if 'tickets' not in data:
            data['tickets'] = []

        return data
    else:
        raise Exception("Erro ao obter dados da API")

def update_data(data):
    # Atualiza o JSON apenas no nível certo, sem aninhamento
    response = requests.put(BASE_URL, headers=HEADERS, json={"record": data})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Erro ao atualizar dados na API")
    

def get_next_ticket_id():
    data = get_data()
    return data['last_ticket_id']


def create_ticket(ticket_type, is_priority):
    data = get_data()
    new_ticket_id = data['last_ticket_id'] + 1
    ticket = {
        "id": new_ticket_id,
        "type": ticket_type,
        "priority": is_priority,
        "called": False
    }
    data['last_ticket_id'] = new_ticket_id
    data['tickets'].append(ticket)
    update_data(data)
    return ticket



def get_called_tickets():
    data = get_data()
    return [ticket for ticket in data['tickets'] if ticket['called']]

def test_api():
    try:
        print("Última senha emitida:", get_next_ticket_id())
        ticket = create_ticket("Caixa", True)
        print("Nova senha emitida:", ticket)
        called_tickets = get_called_tickets()
        print("Senhas chamadas:", called_tickets)
    except Exception as e:
        print("Erro ao testar a API:", e)

# Exemplo de uso:
#test_api()

