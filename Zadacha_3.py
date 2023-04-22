class Client:
    def __init__(self, name: str, account_number: str, balance: int):
        self.name = name
        self.account_number = account_number
        self.balace = balance

class Bank:
    def __init__(self, name: str):
        self.name = name
        self.clients = list()

    def add_client(self, client):
        self.clients.append(client)

    def remove_client(self, client):
        if client in self.clients:
            self.clients.remove(client)

    def find_client_by_name(self, name):
        for client in self.clients:
            if client.name == name:
                print(client)
                return
        print(f'Клиент {name} не найдем')

    def average_balance(self):
        if not self.clients:
            print('Ошибка!')
            return
        total_balance = sum(
            [client.balance for client in self.clients]
        )
        print(total_balance / len(total_balance))

        