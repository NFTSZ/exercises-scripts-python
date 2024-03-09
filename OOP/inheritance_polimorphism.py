# Inheritance and Polimorphism
# With Inheritance, a new class can inherit methods/attributes from 
# a parent class. Along with Polymorphism, the child class reimplements
# the same inherited methods with its own characteristics.

# Creation of the parent class and its methods/attributes
class Animal:
  def __init__(self, name):
    self.name = name

  def andar(self):
    print(f"O animal {self.name} andou.")
    return

  def emitir_som(self):
    pass

# Inheritance and Polimorphism
# Inherits the method from the parent class and implements its own characteristics
class Cachorro(Animal):
  def emitir_som(self):
    return "au-au"

class Gato(Animal):
  def emitir_som(self):
    return "miau"

dog = Cachorro("Cachorro")
cat = Gato("Gato")

pets = [dog, cat]

for animais in pets:
  animais.andar()
  print(f"{animais.name} fez: {animais.emitir_som()}")