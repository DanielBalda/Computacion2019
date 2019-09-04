import unittest
from coffee_maker import (
    cafeteraBasica,
    cafeteraPremium
)


class Cafetera_Basica(unittest.TestCase):
    def setUp(self):
        self.cafeB = cafeteraBasica()

    def test_cafe_solo(self):
        self.assertEqual(self.cafeB.cafetera(1), 'Haciendo cafe')
        self.assertEqual(self.cafeB.aguaCant(10), 'Con 10ml de agua')
        self.assertEqual(self.cafeB.cafeCant(5), 'Con 5g de cafe')
        self.assertEqual(self.cafeB.azucarCant(0), 'Sin azucar')

    def test_cafe(self):
        self.assertEqual(self.cafeB.cafetera(1), 'Haciendo cafe')
        self.assertEqual(self.cafeB.aguaCant(10), 'Con 10ml de agua')
        self.assertEqual(self.cafeB.cafeCant(7), 'Con 7g de cafe')
        self.assertEqual(self.cafeB.azucarCant(3), 'Con 3g de azucar')

    #Hacemos de cuenta que el producto en la cafetera es menor a la que necesita el vaso
    def test_cafe_agua_insuficiente(self):
        self.assertEqual(self.cafeB.cafetera(1), 'Haciendo cafe')
        self.assertEqual(self.cafeB.aguaCant(9999), 'No hay agua suficiente')

    def test_cafe_cafe_insuficiente(self):
        self.assertEqual(self.cafeB.cafetera(1), 'Haciendo cafe')
        self.assertEqual(self.cafeB.aguaCant(10), 'Con 10ml de agua')
        self.assertEqual(self.cafeB.cafeCant(9999), 'No hay cafe suficiente')

    def test_cafe_azucar_insuficiente(self):
        self.assertEqual(self.cafeB.cafetera(1), 'Haciendo cafe')
        self.assertEqual(self.cafeB.aguaCant(10), 'Con 10ml de agua')
        self.assertEqual(self.cafeB.cafeCant(5), 'Con 5g de cafe')
        self.assertEqual(self.cafeB.azucarCant(9999), 'No hay azucar suficiente')


class Cafetera_Premium(unittest.TestCase):
    def setUp(self):
        self.cafeA = cafeteraPremium()

    def test_cafe_solo_con_leche(self):
        self.assertEqual(self.cafeA.vasoSN(True, 1), 'Haciendo cafe')
        self.assertEqual(self.cafeA.aguaCantP(10), 'Con 10ml de agua')
        self.assertEqual(self.cafeA.cafeCantP(5), 'Con 5g de cafe')
        self.assertEqual(self.cafeA.azucarCantP(0), 'Sin azucar')
        self.assertEqual(self.cafeA.lecheCant(True), 'Con leche')

    def test_cafe_sin_vaso(self):
        self.assertEqual(self.cafeA.vasoSN(False, 1), 'Ponga un vaso')

    def test_cafe_sin_leche(self):
        self.assertEqual(self.cafeA.vasoSN(True, 1), 'Haciendo cafe')
        self.assertEqual(self.cafeA.aguaCantP(7), 'Con 7ml de agua')
        self.assertEqual(self.cafeA.cafeCantP(3), 'Con 3g de cafe')
        self.assertEqual(self.cafeA.azucarCantP(2), 'Con 2g de azucar')
        self.assertEqual(self.cafeA.lecheCant(False), 'Sin leche')
        


if __name__ == "__main__":
    unittest.main()