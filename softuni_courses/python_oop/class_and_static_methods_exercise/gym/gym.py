class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = [i for i in self.subscriptions if i.id == subscription_id][0]
        customer = [i for i in self.customers if subscription.customer_id == i.id][0]
        trainer = [i for i in self.trainers if subscription.trainer_id == i.id][0]
        plan = [i for i in self.plans if subscription.exercise_id == i.id][0]
        equipment = [i for i in self.equipment if plan.equipment_id == i.id][0]

        return '\n'.join([str(subscription), str(customer), str(trainer), str(equipment), str(plan)])
