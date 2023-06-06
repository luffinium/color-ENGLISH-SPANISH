looping = True
while looping:
	userColor = input(
    "Your color choices are red,blue,green,white or yellow."
    "\n"
    "Enter a color from the list above:"
    ).lower()
	validColor = True
	if userColor == "red":
		spanishColor = "rojo"
	elif userColor == "blue":
		spanishColor = "azul"	
	elif userColor == "green":
		spanishColor = "verde"
	elif userColor == "white":
		spanishColor = "blanco"	
	elif userColor == "yellow":
		spanishColor = "amarillo"
	else:
		validColor = False
	if validColor:
		print ("The color", userColor, "in Spanish is " + spanishColor)
	else:
		print("That is not a valid for this program.Ese no un color valido.")
		looping = False
	
