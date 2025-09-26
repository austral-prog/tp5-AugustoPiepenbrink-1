def number_to_month(month):

	meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
	
	if 1 <= month <= 12:
		
		return meses [month - 1]

	else:
		
		return "error"
	
numero_de_mes = int(input("Ingresá un número del 1 al 12 para saber el mes:"))

mes = number_to_month(numero_de_mes)
print(f"El mes es: {mes}")
