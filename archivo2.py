print(__name__)

if __name__ == "__main__":
    print(f"Ejecutando desde archivo principal con __name__={__name__}")
elif __name__ == "otra cosa":
    print("Otra cosa dada")
else:
    print("Ejecutando desde archivo importado_ voy a verifificar conflictos")
    print("Ejecutando desde archivo importado_ voy a verifificar conflictos")

