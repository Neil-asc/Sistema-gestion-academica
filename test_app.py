import unittest
from app import calcular_promedio, evaluar_estado_estudiante

class PruebasSistemaAcademico(unittest.TestCase):

    def test_calcular_promedio(self):
        self.assertEqual(calcular_promedio([10, 14, 18]), 14.0)
        self.assertEqual(calcular_promedio([]), 0)

    def test_evaluar_estado_aprobado(self):
        self.assertEqual(evaluar_estado_estudiante(15), "Aprobado")

    def test_evaluar_estado_desaprobado(self):
        self.assertEqual(evaluar_estado_estudiante(10), "Desaprobado")

if __name__ == "__main__":
    unittest.main()
    