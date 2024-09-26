'''
This program allows you to manage data of a company's employees
'''

#Creating the class with the employee information. The following classes inherit from this function
class Empleado:
    def __init__(self, nombre, apellido, salario_base_horas):
        self.nombre = nombre
        self.apellido = apellido
        self.salario_base_horas = salario_base_horas

#Class to calculate the salary of a full-time employee
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, apellido, salario_base_horas):
        super().__init__(nombre, apellido, salario_base_horas)
        self.bono_anual = 2500
        self.sueldo_total = 0
        self.horas = 40
      
#Function to calculate the annual salary + bonus of an employee
    def sueldo_completo(self):
        self.sueldo_total = (self.salario_base_horas * self.horas * 52.1429) + self.bono_anual
        print(f'El sueldo total anual del empleado {self.nombre} es: {self.sueldo_total} Euros.')   

#Class to calculate the salary of a part time employee
class EmpleadoTiempoParcial(Empleado):
    def __init__(self, nombre, apellido, salario_base_horas):
        super().__init__(nombre, apellido, salario_base_horas)
        self.sueldo_total = 0
        self.horas = 20

#Function to calculate the annual salary of an employee
    def sueldo_parcial(self):
        self.sueldo_total = self.salario_base_horas * self.horas * 52.1429
        print(f'El sueldo total anual del empleado {self.nombre} es: {self.sueldo_total} Euros.')

#Example of use
empleado1 = EmpleadoTiempoCompleto('Juan', 'Gómez', 20)
empleado2 = EmpleadoTiempoParcial('Pepe', 'Pérez', 20)

empleado1.sueldo_completo()
empleado2.sueldo_parcial()
