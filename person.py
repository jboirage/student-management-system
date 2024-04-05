#Define abstract Person class - person.py
from abc import ABC
from abc import abstractmethod

class Person(ABC):
    @abstractmethod
    def display_info(self):
        """Abstract method to display information about a person."""
        pass
