from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name, last_name, driving_license_number):
        for i in self.users:
            if i.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."

        self.users.append(User(first_name, last_name, driving_license_number))

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type, brand, model, license_plate_number):
        if vehicle_type not in ('PassengerCar', 'CargoVan'):
            return f"Vehicle type {vehicle_type} is inaccessible."

        for i in self.vehicles:
            if i.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."

        if vehicle_type == 'PassengerCar':
            self.vehicles.append(PassengerCar(brand, model, license_plate_number))
        else:
            self.vehicles.append(CargoVan(brand, model, license_plate_number))

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point, end_point, length):
        for i in self.routes:
            if i.start_point == start_point and i.end_point == end_point and i.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

            elif i.start_point == start_point and i.end_point == end_point and i.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

            elif i.start_point == start_point and i.end_point == end_point and i.length > length:
                i.is_locked = True

        self.routes.append(Route(start_point, end_point, length, len(self.routes) + 1))

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."


