class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while True:
    email = input()
    if email == 'End':
        break

    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')

    if len(email.split('@')[0]) < 5:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = email.split('.')[-1]
    if domain not in ('com', 'bg', 'org', 'net'):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")