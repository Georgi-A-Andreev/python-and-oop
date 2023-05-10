class Customer:
    ID = 1

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.generate_id() - 1

    @staticmethod
    def generate_id():
        Customer.ID += 1
        return Customer.ID

    @staticmethod
    def get_next_id():
        return Customer.ID

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
