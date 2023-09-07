vehiculos=[]
estado=True
i=0
while estado==True:
    i=i+1
    vehiculo={}
    opcion=int(input(" 1. eliminar\n 2. actualizar \n 3. consultar \n 4. agregar \n"))
    if(opcion==1):
        key=(input("que carro desea eliminar (nombre)")) 
        vehiculos.remove(key)   
        print("vehiculo eliminado exitosamente")
    elif(opcion==2):
        actualizarKey=(input("cual vehiculo desea actualizar(nombre)"))
        posicion=vehiculos.index(actualizarKey)
        nombre=(input("cual es el nombre de tu vehiculo: "))
        vehiculos[posicion]=nombre       
    elif(opcion==3):
        consultaID=(input("cual vehiculo desea consultar"))
        posicion=vehiculos.index(actualizarKey)
        print(vehiculos[posicion])
    elif(opcion==4):
        nombre=(input("cual es el nombre de tu vehiculo: "))
        vehiculos.append(nombre)
    respuesta = input("¿desea continuar? (s/n): ")
    estado = True if respuesta.lower() == 's' else False   
print (vehiculos)       
        