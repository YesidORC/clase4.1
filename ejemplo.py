import archivo2 import *

def main():
    sis = Sistema() 
    #probemos lo que llevamos programado
    while True:
        #TAREA HACER EL MENU
        opcion = int(input("\n Ingrese:\n 0 para salir\n 1 para ingresar nuevo paciente\n 2 Ver Paciente\n 3 Para Borrar paciente \n")) 
        if opcion == 1:
            #ingreso pacientes
            print("A continuacion se solicitaran los datos ...") 
            #1. Se solicitan los datos
            nombre = input("Ingrese el nombre: ") 
            cedula = int(input("Ingrese la cedula: ")) 
            genero = input("Ingrese el genero: ") 
            servicio = input("Ingrese el servicio: ") 
            #2. se crea un objeto Paciente
            pac = Paciente() 
            #como el paciente esta vacio debo ingresarle la informacion
            pac.asignarCedula(cedula) 
            pac.asignarGenero(genero) 
            pac.asignarNombre(nombre) 
            pac.asignarServicio(servicio) 
            #3. se almacena en la lista que esta dentro de la clase sistema
            sis.ingresarPaciente(pac)


if __name__=="__main__":
    print("Ejecutando desde archivo principal")
    main()
