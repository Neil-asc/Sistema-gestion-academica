# Sistema Academico Innovatec Education

def calcular_promedio(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

def evaluar_estado_estudiante(promedio):
    if promedio >= 12:
        return "Aprobado"
    else:
        return "Desaprobado"

if __name__ == "__main__":
    print("=== SISTEMA DE GESTION ACADEMICA - INNOVATEC EDUCATION ===")
    mis_notas = [14, 16, 15]
    prom = calcular_promedio(mis_notas)
    est = evaluar_estado_estudiante(prom)
    print(f"Notas registradas: {mis_notas}")
    print(f"Promedio final: {prom:.2f}")
    print(f"Resultado del alumno: {est}")
