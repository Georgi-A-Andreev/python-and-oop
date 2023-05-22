from project2.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    def __init__(self, brand, model, license_plate_number):
        super().__init__(brand, model, license_plate_number, 180)

    def drive(self, mileage):
        self.battery_level -= round((mileage / self.max_mileage) * 100 + 5)
