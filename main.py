import requests
import json

# Airtable
base_id = 'appvVrMPro9b2wo5S'
table_name = 'Tasks'
token_airtable = 'patIkwqUxPFyP03oQ.e28446a815d9e63b58958aca4ffa1bc65e3c82b32004857a1b19a3f27445b86f'
headers_airtable = {"Content-Type": "application/json", "Authorization": f"Bearer {token_airtable}"}
base_url_airtable = f'https://api.airtable.com/v0/{base_id}/{table_name}'

# Calendly
user_id_user = 'https://api.calendly.com/users/2211a9d3-98ea-4a82-bbc0-e67d3be6b598'
user_id_admin = 'https://api.calendly.com/users/f55e5fb2-cbd1-4932-8faf-28566e6a6d13'
base_url_calendly = 'https://api.calendly.com'
token_calendly = 'eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzExODg2NjA3LCJqdGkiOiIwNzg3ODEzNS01MDQxLTQ0OWQtOTdmYi1iYjdlMTcyZTQxM2EiLCJ1c2VyX3V1aWQiOiJmNTVlNWZiMi1jYmQxLTQ5MzItOGZhZi0yODU2NmU2YTZkMTMifQ.sTZ3dhjNkI24Oeu8Crq3YxqFDnxhoiPFvyxWGRRPhFqEZMMO3kci7cDOSLoG-CmSvlMvgT6mkn-ORrdIdI0ZeA'
token_clendly_2 = 'eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzExODk5NDQ3LCJqdGkiOiIzYTY2ZjJkNi0zYWYyLTRhYmItOWM1Ni0zMzEzNzdlMzExNTciLCJ1c2VyX3V1aWQiOiJmNTVlNWZiMi1jYmQxLTQ5MzItOGZhZi0yODU2NmU2YTZkMTMifQ.lHAvFlsYM2h39zSkdL-3v5TRTiXBiIgLtBvREF5nN3D7HhRpVRe8ZkJFUX9ORhBu_NjfGVsCkHW2wjS6tATlaw'
headers_calendly = {"Content-Type": "application/json", "Authorization": f"Bearer {token_calendly}"}


# Função para listar todos os registros
def list_records():
    url = base_url_airtable
    response = requests.get(url, headers=headers_airtable)
    return response.json()

# Função para obter um registro específico
def get_record(record_id):
    url = f'{base_url_airtable}/{record_id}'
    response = requests.get(url, headers=headers_airtable)
    return response.json()

# Função para atualizar um registro
def update_record(record_id, data):
    url = f'{base_url_airtable}/{record_id}'
    response = requests.put(url, headers=headers_airtable, json=data)
    return response.json()

# Função para criar um novo registro
def create_record(data):
    url = base_url_airtable
    response = requests.post(url, headers=headers_airtable, json=data)
    return response.json()

# Função para excluir um registro
def delete_record(record_id):
    url = f'{base_url_airtable}/{record_id}'
    response = requests.delete(url, headers=headers_airtable)
    return response.json()


# Funções do calendly
# Identificar usuário autenticado
def my_user():
    url = f'{base_url_calendly}/users/me'
    response = requests.get(url, headers=headers_calendly)
    return response.json()

# Verificar agendamentos marcados
def user_busy_time(data):
    url = f'{base_url_calendly}/user_busy_times'
    response = requests.get(url, headers=headers_calendly, json=data)
    return response.json()

# Verificar horários disponíveis na agenda
def list_user_availability_schedules(data):
    url = f'{base_url_calendly}/user_availability_schedules'
    response = requests.get(url, headers=headers_calendly, json=data)
    return response.json()

def create_one_off_event_types(data):
    url = f'{base_url_calendly}/one_off_event_types'
    response = requests.post(url, headers=headers_calendly, json=data)
    return response.json()

# Exemplos de uso das funções
if __name__ == '__main__':

    # Escolha a api que deseja consultar
    print("Escolha qual api deseja esecutar:")
    print("1. Airtable")
    print("2. Calendly")
    result = input("Digite o número da opção desejada: ")

    match result:
        case '1':
            # Escolha a função que deseja executar
            print("Escolha a função que deseja executar:")
            print("1. Listar registros")
            print("2. Obter um registro específico")
            print("3. Atualizar um registro")
            print("4. Criar um novo registro")
            print("5. Excluir um registro")
            choice = input("Digite o número da opção desejada: ")

            match choice:
                case '1':
                    print("Listando registros:")
                    print(list_records())
                case '2':
                    record_id = input("Digite o ID do registro que deseja obter: ")
                    print(f"\nObtendo o registro com ID {record_id}:")
                    print(get_record(record_id))
                case '3':
                    record_id = input("Digite o ID do registro que deseja atualizar: ")
                    name = input("Digite o novo nome: ")
                    deadline = input("Digite a nova data no formato (yyyy-mm-dd): ")
                    priority = input("Escolha um nível de prioridade (Low, Medium, High): ")
                    status = input("Escolha um status (In progress, To do, Done): ")

                    data = {
                        "fields": {
                            "Name": name,
                            "Deadline": deadline,
                            "Priority": priority,
                            "Status": status
                        }
                    }
                    print(f"\nAtualizando o registro com ID {record_id}:")
                    print(update_record(record_id, data))
                case '4':
                    name = input("Digite o novo nome: ")
                    deadline = input("Digite a nova data no formato (yyyy-mm-dd): ")
                    priority = input("Escolha um nível de prioridade (Low, Medium, High): ")
                    status = input("Escolha um status (In progress, To do, Done): ")

                    data = {
                        "fields": {
                            "Name": name,
                            "Deadline": deadline,
                            "Priority": priority,
                            "Status": status
                        }
                    }
                    print("\nCriando um novo registro:")
                    print(create_record(data))
                case '5':
                    record_id = input("Digite o ID do registro que deseja excluir: ")
                    print(f"\nExcluindo o registro com ID {record_id}:")
                    print(delete_record(record_id))
                case _:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
        case '2':
            print("Escolha a função que deseja executar:")
            print("1. Meu usuário")
            print("2. Horários Agendados")
            print("3. Horários disponíveis na agenda")
            print("4. Criar uma reunião")

            choice = input("Digite o número da opção desejada: ")

            match choice:
                case "1":
                    print(my_user())
                case "2":
                    user = input("Informe o ID do usuário: ")
                    startTime = "2024-04-16T20:30:00.000000Z"
                    endTime = "2024-04-17T20:30:00.000000Z"
                    data = {
                        "user": user,
                        "start_time": startTime,
                        "end_time": endTime
                    }
                    print(user_busy_time(data))
                case "3":
                    user = input("Informe o ID do usuário: ")
                    data = {
                        "user": user
                    }
                    print(f"\nCarregando as datas disponíveis: ")
                    print(list_user_availability_schedules(data))
                case "4":
                    name = input("Informe o nome da reunião: ")
                    duration = input("Informe a duração da reunião (in minutes): ")
                    start_time = input("Informe o primeiro dia do período (yyyy-mm-dd): ")
                    end_time = input("Informe o último dia do período (yyyy-mm-dd): ")

                    data = {
                          "name": name,
                          "host": "https://api.calendly.com/users/f55e5fb2-cbd1-4932-8faf-28566e6a6d13",
                          "co_hosts": [
                              "https://api.calendly.com/users/2211a9d3-98ea-4a82-bbc0-e67d3be6b598"
                          ],
                          "duration": int(duration),
                          "timezone": "Brazil/West",
                          "date_setting": {
                              "type": "date_range",
                              "start_date": start_time,
                              "end_date": end_time
                          },
                          "location": {
                              "kind": "physical",
                              "location": "Main Office",
                              "additonal_info": "string"
                          }
                    }

                    result = create_one_off_event_types(data)

                    print(result)
                    print(f"Metting name: {result['resource']['name']}")
                    print(f"Scheduling url: {result['resource']['scheduling_url']}")
                    print(f"Location: {result['resource']['locations'][0]['location']}")
                    print(f"Questions: {result['resource']['custom_questions'][0]['name']}")
                    print(f"Event Owner: {result['resource']['profile']['name']}")
                    print(f"Uri: {result['resource']['uri']}")

                case _:
                    print("Opção inválida. Por favor, escolha uma opção válida.")


# {'resource': {'active': True, 'admin_managed': False, 'booking_method': 'instant', 'color': '#0069ff', 'created_at': '2024-03-31T15:35:14.214618Z', 'custom_questions': [{'answer_choices': [], 'enabled': True, 'include_other': False, 'name': 'Please share anything that will help prepare for our meeting.', 'position': 0, 'required': False, 'type': 'text'}], 'deleted_at': None, 'description_html': None, 'description_plain': None, 'duration': 45, 'internal_note': None, 'kind': 'solo', 'locations': [{'additional_info': None, 'kind': 'physical', 'location': 'Main Office'}], 'name': 'Front End Senior Meeting', 'pooling_type': 'collective', 'position': 0, 'profile': {'name': 'Matheus Kobayashi', 'owner': 'https://api.calendly.com/users/f55e5fb2-cbd1-4932-8faf-28566e6a6d13', 'type': 'User'}, 'scheduling_url': 'https://calendly.com/d/ckzw-bfs-gpf/front-end-senior-meeting', 'secret': True, 'slug': 'kz_fjj4d', 'type': 'AdhocEventType', 'updated_at': '2024-03-31T15:35:14.214618Z', 'uri': 'https://api.calendly.com/event_types/6353cabd-0fb9-486c-b213-0da6c87d4bcf'}}
# Metting name: Front End Senior Meeting
# Scheduling url: https://calendly.com/d/ckzw-bfs-gpf/front-end-senior-meeting
# Location: Main Office
# Questions: Please share anything that will help prepare for our meeting.
# Event Owner: Matheus Kobayashi
# Uri: https://api.calendly.com/event_types/6353cabd-0fb9-486c-b213-0da6c87d4bcf