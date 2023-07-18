import doctest
class ConversorTemperatura:
    def __init__(self):
        self.celsius = None
        self.fahrenheit = None

    def seleciona_conversor(self, botao):
        if botao == 1:
            self.conversor_celsius_fahrenheit()
        elif botao == 2:
            self.conversor_fahrenheit_celsius()
        else:
            print("Opção inválida.")

    def conversor_celsius_fahrenheit(self):
        """
        Converte graus Celsius para Fahrenheit.

        >>> teste1 = ConversorTemperatura()
        >>> teste1.celsius = 25
        >>> teste1.conversor_celsius_fahrenheit()
        25° C = 77.0° F.

        >>> teste2 = ConversorTemperatura()
        >>> teste2.celsius = 'a'
        >>> teste2.conversor_celsius_fahrenheit()
        Valor inválido. Insira um valor numérico para os graus Celsius.
        """
        if self.celsius is None:
            celsius_input = input("Digite o valor em graus Celsius: ")
            if self.valida_numero(celsius_input):
                self.celsius = float(celsius_input)
            else:
                print("Valor inválido. Insira um valor numérico para os graus Celsius.")
                return

        try:
            fahrenheit = (self.celsius * 1.8) + 32
            print(f"{self.celsius}° C = {fahrenheit}° F.")
        except TypeError:
            print("Valor inválido. Insira um valor numérico para os graus Celsius.")


    def conversor_fahrenheit_celsius(self):

        """
        Converte graus Fahrenheit para Celsius.

        >>> teste1 = ConversorTemperatura()
        >>> teste1.fahrenheit = 32
        >>> teste1.conversor_fahrenheit_celsius()
        32° F = 0.0° C.

        >>> teste2 = ConversorTemperatura()
        >>> teste2.fahrenheit = 'a'
        >>> teste2.conversor_fahrenheit_celsius()
        Valor inválido. Insira um valor numérico para os graus Fahrenheit.

        """

        if self.fahrenheit is None:
            fahrenheit_input = input("Digite o valor em graus Fahrenheit: ")
            if self.valida_numero(fahrenheit_input):
                self.fahrenheit = float(fahrenheit_input)
            else:
                print("Valor inválido. Insira um valor numérico para os graus Fahrenheit.")
                return
        try:
            celsius = (self.fahrenheit - 32) / 1.8
            print(f"{self.fahrenheit}° F = {celsius}° C.")
        except TypeError:
            print("Valor inválido. Insira um valor numérico para os graus Fahrenheit.")

    @staticmethod
    def valida_numero(valor):
        try:
            float(valor)
            return True
        except ValueError:
            return False
        
doctest.testmod()
print("Conversão de temperaturas")
seleciona_conversor_entrada = int(input("Digite '1' (Celsius para Fahrenheit) ou '2' (Fahrenheit para Celsius): "))

conversor_entrada = ConversorTemperatura()

if seleciona_conversor_entrada == 1:
    conversor_entrada.seleciona_conversor(1)
elif seleciona_conversor_entrada == 2:
    conversor_entrada.seleciona_conversor(2)
else:
    print("Opção inválida.")
