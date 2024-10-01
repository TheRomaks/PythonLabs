from abc import ABC, abstractmethod

class Statistics(ABC):

    @abstractmethod
    def calculate_statistics(self):
        pass