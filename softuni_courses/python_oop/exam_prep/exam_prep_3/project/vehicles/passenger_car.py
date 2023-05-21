from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    def __init__(self,brand, model, license_plate_number):
        super().__init__(brand, model, license_plate_number, 450)

    def drive(self, mileage):
        self.battery_level -= int((mileage / self.max_mileage) * 100)

