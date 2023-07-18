import doctest
class Fibonacci:
    def calcular_termo(self, n):
        """
        Calcula o enésimo termo da série de Fibonacci.

        >>> fibonacci = Fibonacci()
        >>> fibonacci.calcular_termo(6)
        8

        >>> fibonacci.calcular_termo(-2)
        Erro: n deve ser maior do que 0.

        >>> fibonacci.calcular_termo('a')
        Erro: Entre com um número inteiro positivo.

        """
        try:
            n = int(n)
            if n < 0:
                print("Erro: n deve ser maior do que 0.")
                return None
        except ValueError:
            print("Erro: Entre com um número inteiro positivo.")
            return None

        if n == 0 :
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return self.calcular_termo(n-1) + self.calcular_termo(n-2)
        
doctest.testmod()
n = input("Informe um número inteiro maior do que zero: ")

Programa_Fibonacci = Fibonacci()

resultado = Programa_Fibonacci.calcular_termo(n)
if resultado is not None:
    print(resultado)
