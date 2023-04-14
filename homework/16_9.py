class Client:
    def __init__(self, f_name, s_name, city, balance):
        self.f_name = f_name
        self.s_name = s_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'"{self.f_name} {self.s_name}", {self.city}, Баланс: {self.balance} руб.'


client_1 = Client('Max', 'Maceev', 'Perm', 200)
print(client_1)