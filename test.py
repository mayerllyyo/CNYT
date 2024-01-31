import unittest
import operaciones
import math

class TestCplxMethods(unittest.TestCase):

    def test_suma(self):
        c1 = (5.6, -8.9)
        c2 = (-3.4, 6.2)
        self.assertAlmostEqual(operaciones.suma(c1, c2)[0], 2.2)
        self.assertAlmostEqual(operaciones.suma(c1, c2)[1], -2.7)

    def test_producto(self):
        c1 = (3, 2)
        c2 = (-1, 4)
        self.assertAlmostEqual(operaciones.Producto(c1, c2)[0], -11)
        self.assertAlmostEqual(operaciones.Producto(c1, c2)[1], 10)

    def test_resta(self):
        c1 = (5, 7)
        c2 = (3, -2)
        self.assertAlmostEqual(operaciones.resta(c1, c2)[0], 2)
        self.assertAlmostEqual(operaciones.resta(c1, c2)[1], 9)

    def test_division(self):
        c1 = (12, 1)
        c2 = (1, 4)
        self.assertAlmostEqual(operaciones.Division(c1, c2)[0], 0)
        self.assertAlmostEqual(operaciones.Division(c1, c2)[1], 0)

    def test_modulo(self):
        c = (3, 4)
        self.assertAlmostEqual(operaciones.Modulo(c), 5)

    def test_conjugado(self):
        c = (2, -3)
        self.assertEqual(operaciones.conjugado(c), (2, 3))

    def test_polar_a_cartesiano(self):
        polar = (2, math.pi / 3)
        self.assertAlmostEqual(operaciones.polar_a_cartesiano(polar)[0], 1)
        self.assertAlmostEqual(operaciones.polar_a_cartesiano(polar)[1], math.sqrt(3))

    def test_cartesiano_a_polar(self):
        cartesiano = (5,-2)
        self.assertAlmostEqual(operaciones.cartesiano_a_polar(cartesiano)[0], math.sqrt(2))
        self.assertAlmostEqual(operaciones.cartesiano_a_polar(cartesiano)[1], math.pi/4)

    def test_fase(self):
        c = (1, 1)
        self.assertAlmostEqual(operaciones.fase(c), math.pi / 4)


if __name__ == '__main__':
    unittest.main()
