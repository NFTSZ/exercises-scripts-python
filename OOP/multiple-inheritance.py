# Multiple Inheritance:
# Multiple inheritance allows us to inherit from several different classes and 
# have access to all methods and attributes in a chain.

class Animal:
  def __init__(self, nome):
    self.nome = nome
  
  def emitir_som(self):
    pass

class Mamifero(Animal):
  def amamentar(self):
    return f"{self.nome} esta amamentando"

class Ave(Animal):
  def voa(self):
    return f"{self.nome} esta voando"

# this class inherits from both the Mamifero class and the Ave class
# therefore it is a multiple inheritance
class Morcego(Mamifero, Ave):
  def emitir_som(self):
    super().emitir_som()
    return "Morcegos emitem sons supersonicos"

animal = Morcego("Batman")
print(f"Nome do morcego: {animal.nome}")
print(f"Som que ele emite: {animal.emitir_som()}")
print(f"{animal.amamentar()}")
print(f"{animal.voa()}")