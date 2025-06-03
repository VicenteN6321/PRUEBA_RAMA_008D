materia = ['matematicas','fisica','quimica','historia','lenguaje']
mat_rep = []

for  mat in  materia:
    nota = float(input(f"Ingrese el promedio final de {mat} "))
    if nota < 4:
        mat_rep.append(mat)
print(mat_rep)         