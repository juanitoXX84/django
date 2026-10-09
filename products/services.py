from decimal import Decimal

class DescuentoStrategy:
    def aplicar_descuento(self, precio):
        return precio

class DescuentoElectronica(DescuentoStrategy):
    def aplicar_descuento(self, precio):
        return precio * Decimal("0.9")  

class DescuentoRopa(DescuentoStrategy):
    def aplicar_descuento(self, precio):
        return precio * Decimal("0.8")  

class DescuentoDefault(DescuentoStrategy):
    def aplicar_descuento(self, precio):
        return precio  # sin descuento
