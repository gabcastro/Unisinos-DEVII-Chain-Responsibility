from abc import ABC, abstractmethod

class Promotion(ABC):
    @abstractmethod
    def handlerDiscount(self, value):
        ...