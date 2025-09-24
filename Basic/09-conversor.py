textot = input("Ingrese temperatura")
Resultadotexto = float(textot)
Pregunta = input("Es fahrenheit (F) o Celsius (C))? :").lower()
print(Pregunta)



if Pregunta == "f":
    print((Resultadotexto - 32)* 5/9)    

elif Pregunta == "c" :
    print((Resultadotexto * 9/5)+32)

else :
    print("escala incorrecta")