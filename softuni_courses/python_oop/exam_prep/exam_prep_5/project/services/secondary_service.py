from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name):
        super().__init__(name, 15)

    def details(self):
        result = f'{self.name} Secondary Service:\nRobots: '

        if not self.robots:
            result += 'none'
        else:
            result += ' '.join(i.name for i in self.robots)

        return result
