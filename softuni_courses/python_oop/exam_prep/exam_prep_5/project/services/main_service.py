from project2.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name):
        super().__init__(name, 30)

    def details(self):
        result = f'{self.name} Main Service:\nRobots: '

        if not self.robots:
            result += 'none'
        else:
            result += ' '.join(i.name for i in self.robots)

        return result
