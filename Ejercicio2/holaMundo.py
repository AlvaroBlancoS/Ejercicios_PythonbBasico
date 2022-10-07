class claseSaludete:
	def cumpleanios(self, anioNacimiento, anioActual):
		return anioActual-anioNacimiento

dato = claseSaludete()
nombre = input("Cómo te llama?\n")
anio = int(input("Pon anio de tu nacimiento\n"))
print("Hola", nombre, ", tienes ",dato.cumpleanios(anio,2022)," anios")
print("Dato de la variable 'nombre': ",type(nombre),"\nDato de la variable 'anio': ",type(anio))

