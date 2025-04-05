class Alumno:
    # Cuando cree un alumno, se proporcionará el nombre y la edad
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
a1 = Alumno("Maria", 20)
a2 = Alumno("Juan", 21)
a3 = Alumno("Ana", 19)  

edad_mayor = 0
edad_menor = 99
if a1.getEdad() > edad_mayor:
    edad_mayor = a1.getEdad()
    alumno_mayor = a1.getNombre()
if a2.getEdad() > edad_mayor:
    edad_mayor = a2.getEdad()
    alumno_mayor = a2.getNombre()
if a3.getEdad() > edad_mayor:
    edad_mayor = a3.getEdad()
    alumno_mayor = a3.getNombre()

print(f'El alumno mayor es {alumno_mayor} y tiene {edad_mayor} años de edad')   

alumnos = [a1, a2, a3] 

nombres = ''
suma = 0
for alum in alumnos:  
    if alum.getEdad() < edad_menor:
        edad_menor = alum.getEdad()
        alumno_menor = alum.getNombre()
    nombres += alum.getNombre() + ' '
    suma += alum.getEdad()

print(f'El alumno menor es {alumno_menor} y tiene {edad_menor} años de edad')   

print(f'Entre {nombres} suman {suma} años')   
