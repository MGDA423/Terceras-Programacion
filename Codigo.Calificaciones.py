class Alumno:
    def __init__(self,Nombre,Materia,Calificaciones):
        self.Nombre = Nombre
        self.Materia = Materia
        self.Calificaciones = Calificaciones

    def promedio(self):
        return sum(self.Calificaciones)/len(self.Calificaciones)
    
    def mostrar_info(self):
        print("---Datos del Alumno---")
        print(f"Nombre:{self.Nombre}")
        print(f"Materia:{self.Materia}")
        print(f"Calificaciones:{self.Calificaciones}")
        print(f"promedio{self.promedio():.2f}")

if __name__ == "__main__":
    Alumnos = []

    while True:
        print("---Menu de Calificaciones---")
        print("1.Agregar Alumno")
        print("2.Ver promedios")
        print("3.Eliminar Alumno")
        print("4.Buscar Alumno")
        print("5.Salir")
        opcion = input("Elige una opcion:  ")

        if opcion == "1":
            Nombre = input("Nombre del alumno: ")
            Materia = input("Materia: ")
            calificaciones = []

            print("Ingresa 5 Calificaciones: ")
            for i in range(5):
                cal = float(input(f"Calificacion {i+1}:"))
                calificaciones.append(cal) 

                alumno = Alumno(Nombre,Materia,calificaciones)
                Alumnos.append(alumno)
                print("Alumno Agregado")

        elif opcion == "2":
            if not Alumnos:
                print("No hay Alumnos registrados")
            else:
                for alumno in Alumnos:
                    alumno.mostrar_info()

        elif opcion == "3":
            if not Alumnos:
                print("No hay alumnos para eliminar")
            else:
                Nombre_eliminar = input("Ingresa el alumno para eliminar: ")
                encontrado = False
                for alumno in Alumnos:
                    if alumno.Nombre == Nombre_eliminar:
                            Alumnos.remove(alumno)
                            print(f"Alumno {Nombre_eliminar} eliminado correctamente.")
                            encontrado = True
                            break
                if not encontrado:
                        print("Alumno no encontrado")

        elif opcion == "4":
            if not Alumnos: 
                print("No hay Alumnos en la Lista")
            else:
                Nombre_buscar = input("Ingresa el Nombre del Alumno a buscar: ")
                encontrado = False
                for alumno in Alumnos:
                    if alumno.Nombre == Nombre_buscar:
                        alumno.mostrar_info()
                        encontrado = True
                        break
                if not encontrado:
                    print("Alumno no encontrado")

        elif opcion == "5":
            print("saliedo del programa")
            break
        else:
            print("Opcion no valida")                

                        