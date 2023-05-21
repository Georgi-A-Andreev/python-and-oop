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

    def make_trip(self, driving_license_number, license_plate_number, route_id, is_accident_happened):
        user = [i for i in self.users if i.driving_license_number == driving_license_number][0]
        vehicle = [i for i in self.vehicles if i.license_plate_number == license_plate_number][0]
        route = [i for i in self.routes if i.route_id == route_id][0]

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return vehicle.__str__()

    def repair_vehicles(self, count):
        result = sorted([i for i in self.vehicles if i.is_damaged], key=lambda x: (x.brand, x.model))

        for i in range(min(count, len(result))):
            result[i].is_damaged = False
            result[i].recharge()

        return f"{min(count, len(result))} vehicles were successfully repaired!"

    def users_report(self):
        result = '*** E-Drive-Rent ***\n'

        for i in sorted(self.users, key= lambda x: x.rating, reverse=True):
            result += str(i)
            result += '\n'

        return result

