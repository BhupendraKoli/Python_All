# ABC is absctract base class 
from abc import ABC ,abstractmethod

class my_claculator(ABC):

    @abstractmethod
    def add (self):
        pass

    @abstractmethod
    def sub(self):
        pass

    @abstractmethod
    def div(self):
        pass

    @abstractmethod
    def mul(self):
        pass

