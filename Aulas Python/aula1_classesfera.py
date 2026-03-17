from dataclasses import dataclass
import math

@dataclass
class Esfera:
    cor: str
    raio: float
    
    # __post_init__ : Esse método roda logo depois que o objeto é criado, usado para validar dados!

    def __post_init__(self):
        # Validação do raio
        if self.raio <= 0:
            raise ValueError("O raio deve ser maior que zero.")

    def volume(self):
        return (4/3) * math.pi * (self.raio ** 3)

    def area(self):
        return 4 * math.pi * (self.raio ** 2)

    def diametro(self):
        return 2 * self.raio
    # __str__ : Define com o objeto aparece quando usamos print().
    def __str__(self):
        return f"Esfera cor={self.cor}, raio={self.raio}"


bola1 = Esfera("vermelha", 4)
bola2 = Esfera("azul", 7)

print(bola1)

print(f"Volume: {bola1.volume():.2f} cm³")
print(f"Área: {bola1.area():.2f} cm²")
print(f"Diâmetro: {bola1.diametro():.2f} cm")