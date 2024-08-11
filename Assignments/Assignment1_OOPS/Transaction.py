from abc import ABC, abstractmethod

class Transaction(ABC):
    def __init__(self, amount, location):
        self.amount = amount
        self.location = location

    @abstractmethod
    def process(self):
        pass
