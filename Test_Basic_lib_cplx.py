import BasicLibcplx as Bclib
import unittest


class TestBasicCplx(unittest.TestCase):

    def test_sum(self):
        suma1 = Bclib.sum_cplx((3, 4),(-1, 2))
        self.assertAlmostEqual(suma1[0], 2)
        self.assertAlmostEqual(suma1[1], 6)

        suma2 = Bclib.sum_cplx((1.23, -2.18),(0.54, 5.22))
        self.assertAlmostEqual(suma2[0], 1.77)
        self.assertAlmostEqual(suma2[1], 3.04)

    def test_mult(self):
        mult1 = Bclib.mult_cplx((3, 4),(-1, 2))
        self.assertAlmostEqual(mult1[0], -11)
        self.assertAlmostEqual(mult1[1], 2)

        mult2 = Bclib.mult_cplx((1.23, -2.18),(0.54, 5.22))
        self.assertAlmostEqual(mult2[0], 12.0438,)
        self.assertAlmostEqual(mult2[1], 5.2434)

    def test_resta(self):
        rest1 = Bclib.diferencia_cplx((3, 4),(-1, 2))
        self.assertAlmostEqual(rest1[0], 4)
        self.assertAlmostEqual(rest1[1], 2)

        rest2 = Bclib.diferencia_cplx((1.23, -2.18),(0.54, 5.22))
        self.assertAlmostEqual(rest2[0], 0.69)
        self.assertAlmostEqual(rest2[1], -7.4)

    def test_divcplx(self):
        div1 = Bclib.division_cplx((3, 4),(-1, 2))
        self.assertAlmostEqual(div1[0], 1)
        self.assertAlmostEqual(div1[1], -2)

        div2 = Bclib.division_cplx((1.23, -2.18),(0.54, 5.22))
        self.assertAlmostEqual(div1[0], 1)
        self.assertAlmostEqual(div1[1], -2)

    def test_modulo(self):
        modulo1 = Bclib.modulo((3,4))
        self.assertAlmostEqual(modulo1, 5)

        modulo2 = Bclib.modulo((5, -2.18))
        self.assertAlmostEqual(modulo2, 5.45457, places=4)

    def test_conjugado(self):
        conj1 = Bclib.conjugado((3, 4))
        self.assertAlmostEqual(conj1[0], 3)
        self.assertAlmostEqual(conj1[1], -4)

        conj2 = Bclib.conjugado((5, -2.18))
        self.assertAlmostEqual(conj2[0], 5)
        self.assertAlmostEqual(conj2[1], 2.18)

    def test_cartopolar(self):
        cart1 = Bclib.cartopolar((3,4))
        self.assertAlmostEqual(cart1[0],5)
        self.assertAlmostEqual(cart1[1],0.9272, places=3)

        cart2 = Bclib.cartopolar((5, -2.18))
        self.assertAlmostEqual(cart2[0], 5.45457, places=4)
        self.assertAlmostEqual(cart2[1], -0.41115, places=4)

    def test_polartocart(self):

        polar1 = Bclib.polartocart((3.605, 0.982793))
        self.assertAlmostEqual(polar1[0], 2, places=3)
        self.assertAlmostEqual(polar1[1], 3, places=3)

        polar2 = Bclib.polartocart((1.414213, 0.785398))
        self.assertAlmostEqual(polar2[0], 1, places=3)
        self.assertAlmostEqual(polar2[1], 1, places=3)


    def test_fase(self):
        fase1 = Bclib.fase((3,4))
        self.assertAlmostEqual(fase1, 0.9272952)

        fase2 = Bclib.fase((-1,-2))
        self.assertAlmostEqual(fase2, -2.03444393)  #4.2484
if __name__ == '__main__':
    unittest.main()
