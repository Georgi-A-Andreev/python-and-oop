class RechargeEnergyMixin:
    def recharge_energy(self, amount):
        self.energy = min(self.energy + amount, 100)

        self.save()
