print("hola mundo")


if __name__ == "__main__":
    print(f"Ejecutando desde archivo principal con __name__={__name__}")

else:
    print(f"Ejcutandose desde importación como archivo secundario __name__={__name__}")