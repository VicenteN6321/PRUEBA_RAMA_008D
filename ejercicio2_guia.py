alumno = []
edad = []
loop_ok = True

alumno_aux = ""
edad_aux = 0

while loop_ok == True:
    nombre =  input("Ingrese el nombre del alumno ")
    if nombre != "*":
        edad_op  =  int(input(f"Ingrese la edad del alumno {nombre} "))
        alumno.append(nombre)
        edad.append(edad_op)
    else:
        loop_ok = False

print("Alumnos mayores a 18 años")
for i in range(len(alumno)):
    if edad[i] >= 18:
        print(alumno[i])

print("Alumnos ordenados por edad de mayor a menor")

for x  in range(len(edad)):
    for y in  range(x+1,len(edad)):
        if edad[x] < edad[y]:
            edad_aux = edad[x]
            edad[x] = edad[y]
            edad[y] =  edad_aux

            alumno_aux = alumno[x]
            alumno[x] = alumno[y]
            alumno[y] =  alumno_aux

for i in range(len(alumno)):
     print(alumno[i])
