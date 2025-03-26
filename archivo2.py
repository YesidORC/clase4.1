class Paciente():
    def __init__(self):
        self.__nombre = '' 
        self.__cedula = 0 
        self.__genero = '' 
        self.__servicio = '' 

class Sistema:
    def __init__(self):
        self.__lista_pacientes = [] 
    def __str__(self):
        return f" {len(self.__lista_pacientes} en el sistema "
    def ingresarPaciente(self,pac):
        self.__lista_pacientes.append(pac) 

if __name__ == "__main__":
    print(f"Ejecutando desde archivo principal con __name__= {__name__}  /
    se crean objetos de para hacer pruebas Paciente y Sistema")
    p =  Paciente()
    hosp =  Sistema()
    hosp.ingresarPaciente(p)
    print(hosp)
elif __name__ == "otra cosa":
    print("Otra cosa dada")
else:
    print("Ejecutando desde archivo importado_ voy a verifificar conflictos")
    


