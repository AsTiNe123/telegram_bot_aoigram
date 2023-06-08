from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def sqwer(self):
        pass
    @abstractmethod  
    def perim(self):
        pass
