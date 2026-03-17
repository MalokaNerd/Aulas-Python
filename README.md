Projeto Python — Classe Esfera

Este projeto demonstra conceitos básicos de Programação Orientada a Objetos (POO) utilizando Python.
O código implementa uma classe chamada Esfera, capaz de calcular propriedades geométricas como volume, área superficial e diâmetro.

O objetivo do projeto é praticar conceitos de:

Classes e objetos

Métodos

Validação de dados

Uso de @dataclass

Operações matemáticas com o módulo math

Estrutura do Projeto
esfera.py
README.md

esfera.py → implementação da classe Esfera

README.md → documentação do projeto

Tecnologias Utilizadas

Python

Biblioteca padrão math

dataclasses (recurso moderno para simplificar classes)


Conceitos Demonstrados
Classe

A classe Esfera representa um modelo de esfera com dois atributos:

cor

raio

@dataclass
class Esfera:
    cor: str
    raio: float
Métodos Implementados
Volume

Calcula o volume da esfera.

𝑉
=
4
3
𝜋
𝑟
3
V=
3
4
	​

πr
3
def volume(self):
    return (4/3) * math.pi * (self.raio ** 3)
Área Superficial

Calcula a área da superfície da esfera.

𝐴
=
4
𝜋
𝑟
2
A=4πr
2
def area(self):
    return 4 * math.pi * (self.raio ** 2)
Diâmetro

Calcula o diâmetro da esfera.

𝐷
=
2
𝑟
D=2r
def diametro(self):
    return 2 * self.raio
Validação de Dados

O método __post_init__ garante que o raio seja maior que zero.

def __post_init__(self):
    if self.raio <= 0:
        raise ValueError("O raio deve ser maior que zero.")
Como Executar

Certifique-se de ter Python instalado.

python3 --version

Execute o arquivo:

python3 esfera.py
 Exemplo de Saída
Esfera cor=vermelha, raio=4
Volume: 268.08 cm³
Área: 201.06 cm²
Diâmetro: 8.00 cm

Objetivo Educacional

Este projeto foi desenvolvido para praticar conceitos fundamentais de:

Programação Orientada a Objetos

Estruturação de código em Python

Modelagem de objetos do mundo real

Também serve como exercício prático para estudantes iniciantes em programação.

Possíveis Melhorias Futuras

Implementar cálculo de densidade

Adicionar testes automatizados

Criar interface gráfica


