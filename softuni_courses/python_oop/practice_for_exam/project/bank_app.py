from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    LOAN_TYPES = {'StudentLoan': StudentLoan, 'MortgageLoan': MortgageLoan}
    CLIENT_TYPES = {'Student': Student, 'Adult': Adult}
    VALID_MATCHES = {'StudentLoan':  'Student', 'MortgageLoan': 'Adult'}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type):
        if loan_type not in self.LOAN_TYPES:
            raise Exception("Invalid loan type!")
        self.loans.append(self.LOAN_TYPES[loan_type]())
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.CLIENT_TYPES:
            raise Exception("Invalid client type!")
        if self.capacity == len(self.clients):
            return "Not enough bank capacity."
        self.clients.append(self.CLIENT_TYPES[client_type](client_name, client_id, income))
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = next(c for c in self.clients if c.client_id == client_id)
        loan = next(l for l in self.loans if l.__class__.__name__ == loan_type)
        if self.VALID_MATCHES[loan_type] != client.__class__.__name__:
            raise Exception("Inappropriate loan type!")
        client.loans.append(loan)
        self.loans.remove(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = next((c for c in self.clients if c.client_id == client_id), None)
        if client is None:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        counter = 0
        for l in self.loans:
            if l.__class__.__name__ == loan_type:
                l.increase_interest_rate()
                counter += 1

        return f"Successfully changed {counter} loans."

    def increase_clients_interest(self, min_rate: float):
        counter = 0
        for c in self.clients:
            if c.interest < min_rate:
                c.increase_clients_interest()
                counter += 1

        return f"Number of clients affected: {counter}."

    def get_statistics(self):
        return f"Active Clients: {len(self.clients)}\n"\
                f"Total Income: {sum(c.income for c in self.clients):.2f}\n"\
                f"Granted Loans: {sum(len(c.loans) for c in self.clients)}, Total Sum: {sum(sum(l.amount for l in c.loans) for c in self.clients):.2f}\n"\
                f"Available Loans: {len(self.loans)}, Total Sum: {sum(l.amount for l in self.loans):.2f}\n"\
                f"Average Client Interest Rate: {sum(c.interest for c in self.clients) / len(self.clients) if self.clients else 0 :.2f}"
