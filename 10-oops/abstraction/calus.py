'''
### Question: Temperature Converter
Create a temperature converter program with the following menu options:
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius

'''
from abc import ABC , abstractmethod

class temp_conv(ABC):
    @abstractmethod
    def cel_to_fah(self):
        pass
    @abstractmethod
    def fah_to_cel(self):
        pass
    @abstractmethod
    def cel_to_kel(self):
        pass
    @abstractmethod
    def kel_to_cel(self):
        pass 