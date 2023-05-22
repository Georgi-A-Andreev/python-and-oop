from typing import List

from project2.robots.base_robot import BaseRobot
from project2.robots.female_robot import FemaleRobot
from project2.robots.male_robot import MaleRobot
from project2.services.base_service import BaseService
from project2.services.main_service import MainService
from project2.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type, name):
        if service_type not in ('MainService', 'SecondaryService'):
            raise Exception("Invalid service type!")

        if service_type == 'MainService':
            self.services.append(MainService(name))
        else:
            self.services.append(SecondaryService(name))

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type, name, kind, price):
        if robot_type not in ('MaleRobot', 'FemaleRobot'):
            raise Exception("Invalid robot type!")

        if robot_type == 'MaleRobot':
            self.robots.append(MaleRobot(name, kind, price))
        else:
            self.robots.append(FemaleRobot(name, kind, price))

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name, service_name):
        robot = [i for i in self.robots if i.name == robot_name][0]
        service = [i for i in self.services if i.name == service_name][0]

        if (isinstance(robot, MaleRobot) and
            isinstance(service, SecondaryService)) or (isinstance(robot, FemaleRobot) and
                                                       isinstance(service, MainService)):
            return "Unsuitable service."

        if service.capacity < 1:
            raise Exception("Not enough capacity for this robot!")

        service.robots.append(robot)
        self.robots.remove(robot)
        service.capacity -= 1

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name, service_name):
        service = [i for i in self.services if i.name == service_name][0]

        if robot_name not in [i.name for i in service.robots]:
            raise Exception("No such robot in this service!")

        robot = [i for i in service.robots if i.name == robot_name][0]

        self.robots.append(robot)
        service.robots.remove(robot)
        service.capacity += 1

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name):
        service = [i for i in self.services if i.name == service_name][0]

        for i in service.robots:
            i.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name):
        service = [i for i in self.services if i.name == service_name][0]

        return f"The value of service {service_name} is {sum([i.price for i in service.robots]):.2f}."

    def __str__(self):
        return '\n'.join([i.details() for i in self.services])


main_app = RobotsManagingApp()
print(main_app.add_service('SecondaryService', 'ServiceRobotsWorld'))
print(main_app.add_service('MainService', 'ServiceTechnicalsWorld'))
print(main_app.add_robot('FemaleRobot', 'Scrap', 'HouseholdRobots', 321.26))
print(main_app.add_robot('FemaleRobot', 'Sparkle', 'FunnyRobots', 211.11))

print(main_app.add_robot_to_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.add_robot_to_service('Sparkle', 'ServiceRobotsWorld'))

print(main_app.feed_all_robots_from_service('ServiceRobotsWorld'))
print(main_app.feed_all_robots_from_service('ServiceTechnicalsWorld'))

print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print(str(main_app))

print(main_app.remove_robot_from_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print(str(main_app))
