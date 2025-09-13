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
       return self.salario > 3000

    def ticket(self):
        print("Ticket de Empleado\n")
        print("---------------------\n")
        print(f"nombre:{self.nombre}\n")
        print(f"departamento:{self.departamento.nombre}\n")
        print(f"puesto:{self.puesto}\n")
        print(f"Fecha de ingreso:{self.fecha_ingreso}\n")
        print(f"salario: ${self.salario}\n" )
        print(f"Paga impuestos?: {'Sí' if self.paga_impuestos() else 'No'}\n")
        print(f"---Datos Extra del Empleado----\n")
        print(f"Direccion:{self.direccion}\n")
        print(f"Telefono:{self.telefono}\n")
        print (f"Hobbies:{self.hobbies}\n")
        print(f"Ciudad:{self.ciudad}\n")
        print(f"-------------- \n")
    
if __name__ == "__main__":
    empleados = []  
#menu
    while True:
        print("Menu de Empleados")
        print("1.Agregar Empleados")
        print("2.Ver ticket de Empleados")
        print("3.Salir")
        opcion = input ("Elige un Numero:  ") 

        if opcion == "1":
            dept_nombre = input("Ingresa el Nombre del Departamento: ")
            departamento = departamento(dept_nombre)

            nombre = input("Nombre del Empleado: ")
            salario = float(input("Salario: "))
            fecha_ingreso = input("Fecha de Ingreso: ")
            direccion = input("Direccion: ")
            telefono = input("Telefono: ")
            puesto = input("Puesto: ")
            hobbies = input("Hobbies: ")
            ciudad = input("Ciudad: ")

            empleado = Empleado(nombre,salario,fecha_ingreso,departamento,direccion,telefono,puesto,hobbies,ciudad)
            empleados.append(empleado)

        elif opcion == "2":
            if not empleados:
                print("No hay Empleados en la Lista")
            else:
                for empleado in empleados:
                    empleado.ticket()
                    
        elif opcion == "3":
            print("Saliendo del Programa...")
            break
        else:
            print("Opcion no Encontrada..")



