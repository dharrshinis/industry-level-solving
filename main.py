from abc import ABC, abstractmethod

class WaterConsumer(ABC):
    def __init__(self, customer_id, consumption, tariff):
        self.customer_id = customer_id
        self.consumption = consumption
        self.tariff = tariff

    @abstractmethod
    def compute_bill(self):
        pass


class ResidentialConsumer(WaterConsumer):
    def compute_bill(self):
        return calculate_slab_bill(self.consumption, self.tariff)


class CommercialConsumer(WaterConsumer):
    def compute_bill(self):
        return calculate_slab_bill(self.consumption, self.tariff)


class IndustrialConsumer(WaterConsumer):
    def compute_bill(self):
        return calculate_slab_bill(self.consumption, self.tariff)
