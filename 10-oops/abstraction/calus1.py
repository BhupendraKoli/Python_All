'''
### Question: Temperature Converter
Create a temperature converter program with the following menu options:
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius

'''
from calus import temp_conv

class coverter(temp_conv):
    def cel_to_fah(self):
        num=float(input("enter the temp for convert Celsius to Fahrenheit :-  "))
        res=(num * 9/5) + 32
        print (f"The Celsius is {num} and Fahrenheit is {res} ")
    def fah_to_cel(self):    
        num=float(input("enter the temp for convert Fahrenheit to Celsius :-  "))
        res=(num - 32) * 5/9
        print (f"The Fahrenhet is {num} and Celsius is {res} ")
    def cel_to_kel(self):
        num=float(input("enter the temp for convert  Celsius to Kelvin :-  "))
        res=num + 273.15
        print (f"The  Celsius  is {num} and Kelvin is {res} ")
    def kel_to_cel(self):
        num=float(input("enter the temp for convert  Kelvin to Celsius :-  "))
        res=num - 273.15
        print (f"The  kelvin  is {num} and celsius is {res} ")


