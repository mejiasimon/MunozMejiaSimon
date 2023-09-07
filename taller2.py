vehiculos={}
estado=True
i=0
while estado==True:
    i=i+1
    vehiculo={}
    opcion=int(input(" 1. eliminar\n 2. actualizar \n 3. consultar \n 4. agregar \n"))
    if(opcion==1):
        key=(input("que carro desea eliminar (id)")) 
        vehiculos.pop(f"vehiculo{key}")     
        print("vehiculo eliminado exitosamente")
    elif(opcion==2):
        actualizarKey=(input("cual vehiculo desea actualizar"))
        nombre2=(input("cual es el nombre de tu vehiculo: "))
        id2=(input("cual es la id de el vehiculo: "))
        marca2=(input("cual es la marca: "))
        potencia2=(input("cuantos caballos de fuerza tiene: "))
        vehiculos[f"vehiculo{actualizarKey}"]["nombre"]=nombre2
        vehiculos[f"vehiculo{actualizarKey}"]["id"]=id2
        vehiculos[f"vehiculo{actualizarKey}"]["marca"]=marca2
        vehiculos[f"vehiculo{actualizarKey}"]["potencia"]=potencia2       
    elif(opcion==3):
        consultaID=(input("cual vehiculo desea consultar"))
        consulta=vehiculos.get(f"vehiculo{consultaID}")
        for x,y in consulta.items():
            print(x,y)
    elif(opcion==4):
        nombre=(input("cual es el nombre de tu vehiculo: "))
        id=(input("cual es la id de el vehiculo: "))
        marca=(input("cual es la marca: "))
        potencia=(input("cuantos caballos de fuerza tiene: "))
        vehiculo["nombre"]=nombre
        vehiculo["id"]=id
        vehiculo["marca"]=id
        vehiculo["potencia"]=id
        vehiculos[f"vehiculo{id}"]=vehiculo
    respuesta = input("¿desea continuar? (s/n): ")
    estado = True if respuesta.lower() == 's' else False   
print (vehiculos)       
        
           
        
  
    