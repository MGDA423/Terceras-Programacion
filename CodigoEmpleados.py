class departamento:
    def __init__(self,nombre):
        self.nombre = nombre

class Empleado:
    def __init__(self,nombre,salario,fecha_ingreso,departamento,direccion,telefono,puesto,hobbies,ciudad):
        self.nombre = nombre
        self.salario = salario
        self.fecha_ingreso = fecha_ingreso
        self.departamento = departamento
        self.direccion = direccion
        self.telefono = telefono
        self.puesto = puesto
        self.hobbies = hobbies
        self.ciudad = ciudad

    def paga_impuestos(self):
        if self.sueldo>3000:
            print("Debe de pagar impuestos")
        else:
            print("No paga impuestos")  

    def ticket(self):
        ticket = "Ticket de Empleado\n"
        ticket += "---------------------\n" 
        ticket += f"nombre:{self.nombre}\n" 
        ticket += f"departamento:{self.departamento.nombre}\n"  
        ticket += f"puesto:{self.puesto}\n"
        ticket += f"Fecha de ingreso:{self.fecha_ingreso}\n" 
        ticket += f"salario: ${self.salario}\n"  
        ticket += f"paga impuestos?:{'Sí' if self.paga_impuestos() else'No'}\n"  
        ticket += f"---Datos Extra del Empleado----\n"
        ticket += f"Direccion:{self.direccion}\n"
        ticket += f"Telefono:{self.telefono}\n"
        ticket += f"Hobbies:{self.hobbies}\n"
        ticket += f"Ciudad:{self.ciudad}\n"
        ticket += f"-------------- \n"
        return ticket
    
if __name__ == "__main__":
    empleados = []  
#menu
    while True:
        print()  