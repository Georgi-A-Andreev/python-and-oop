class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
while True:
    information = input()

    if information == 'Stop':
        break

    information = information.split()
    sender = information[0]
    receiver = information[1]
    content = information[2]
    emails.append(Email(sender, receiver, content))

idx = [int(x) for x in input().split(', ')]

for el in idx:
    emails[el].send()

for el in emails:
    print(el.get_info())




