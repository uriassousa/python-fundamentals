# def somar( x, y):
#     return x + y

# def subtrair( x, y):
#     return x - y

# def multiplicar( x, y):
#     return x * y

# def dividir( x, y):
#     return x / y

# assert somar(2, 2) == 4, "Obtido: {}, Esperado: 4".format(somar(2,2))
# assert somar(3, 3) == 6, "Obtido: {}, Esperado: 4".format(somar(3,3))

# assert subtrair(2, 2) == 0, "Obtido: {}, Esperado: 4".format(subtrair(2,2))
# assert subtrair(5, 3) == 2, "Obtido: {}, Esperado: 4".format(subtrair(5,3))

# assert multiplicar(10, 2) == 20, "Obtido: {}, Esperado: 4".format(multiplicar(10,2))
# assert multiplicar(1, 3) == 3, "Obtido: {}, Esperado: 4".format(multiplicar(1,3))

# assert dividir(10, 2) == 5, "Obtido: {}, Esperado: 4".format(dividir(10,2))
# assert dividir(16, 2) == 8, "Obtido: {}, Esperado: 4".format(dividir(16,2))


from unittest import TestCase, main

def soma(x, y):
    return x + y

def subtrair(x, y):
    return x - y 


class Testes(TestCase):

    def test_soma(self):
        self.assertEqual(soma(5, 5), 10)
        self.assertLess(soma(5, 5),11)
    
    def test_sub(self):
        self.assertEqual(subtrair(5, 5), 0)
        self.assertLessEqual(subtrair(15, 5), 10)

if __name__ == "__main__":
    main()