

def imprimir_mensaje(age, nombre, apellido):
    print("entro al def funtion")
    if age>= 18:
        print('entro al if 18')
        resultadoedad = ('es mayor de edad')
    else:
        resultadoedad = ("es menor de edad")

    #message = first + '  [' + last + '] is a coder '

    msg = f'{nombre} {apellido} is a coder and {resultadoedad}'
    
    msg1 = nombre + ' ' + apellido + ' is a coder ' + resultadoedad
    print(msg)

def imprimir_humano_y_mascota(nombreh, apellidoh, nombrem, apellidom, edadm):
    """quiero que me imprima un mensaje que diga nombre apellido es dueno de nombremacota con edadmacota anos de 
    edad: ejemplo Alexandra agredo es duena de holy con 3 anos de edad
    
    args: 
    nombre de humano
    apellido del humano
    nombre de mascota
    edad mascota
    
    """

    msg_humano_y_mascota = f'{nombreh} {apellidoh} is the owner of {nombrem} {apellidom} , the pet is {edadm} years old'
    print(msg_humano_y_mascota)





def ingresar_datos_de_humano():
    firsth = input("Entrer your name : ")
    lasth = input("enter your last name: ")
    edadh = int(input("enter your age: "))


    return firsth, lasth, edadh

def ingresar_datos_de_mascota():
    firstm = input("Enter the name of your pet: ")
    lastm = input("Enter the last name of your pet: ")
    edadm = int(input("Enter the age of your pet: "))

    return firstm, lastm, edadm


if __name__ == "__main__":
    try:
        print("entro al try")
        #print(ingresar_datos_de_humano())

        first, last, edad = ingresar_datos_de_humano()
        mfirst, mlast, medad = ingresar_datos_de_mascota()

        imprimir_humano_y_mascota(first, last, mfirst, mlast, medad)

    except Exception: 
        print("ERROR INSERT ONLY NUMBERS YOU HAVE ANOTHER TRY")
        pregunta_nueva = input("ENTER (H) IF YOU WANT TO TYPE AGAIN DE INFORMATION FOR THE OWNER OR (M) IF IS THE INFORMATION FOR THE PET ").lower()

        if pregunta_nueva == 'h':
            
            first, last, edad = ingresar_datos_de_humano()
            
            mfirst, mlast, medad = ingresar_datos_de_mascota()
            imprimir_humano_y_mascota(first, last, mfirst, mlast, medad)
        
        elif pregunta_nueva == 'm':
            mfirst, mlast, medad = ingresar_datos_de_mascota()
        
            first, last, edad = ingresar_datos_de_humano()
            imprimir_humano_y_mascota(first, last, mfirst, mlast, medad)


        else:
            print("ERROR ERROR")



        
            


        

        














