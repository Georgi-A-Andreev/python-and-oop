class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: " \
               f"{self.content}. Sent: {self.is_sent}"


list = []
while True:
    information = input()
    if information == 'Stop':
        break

    sender, receiver, content = information.split()
    email = Email(sender, receiver, content)
    list.append(email)

indices = input().split(", ")

for i in indices:
    list[int(i)].send()

for i in list:
    print(i.get_info())
