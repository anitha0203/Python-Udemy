from database import Database
from abc import ABCMeta, abstractmethod


class Saveable(metaclass=ABCMeta):
    def save(self):
        Database.insert(self.to_dict())

    @abstractmethod
    def to_dict(self):
        pass
