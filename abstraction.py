# Abstraction:
# Is an important concept that allows us to create a template to 
# build other classes. An abstract class cannot be instantiated 
# directly, but it serves as a template for other classes, when 
# creating a derived class, it is mandatory to implement the methods 
# defined in the abstract class.

from abc import ABC, abstractmethod

class Veiculo(ABC):
  
  @abstractmethod
  def ligar(self):
    pass

  @abstractmethod
  def desligar(self):
    pass

class Carro(Veiculo):
  def __init__(self, nome):
    self.nome = nome
  
  def ligar(self):
    print(f"{self.nome} ligou")
    return

  def desligar(self):
    print(f"{self.nome} desligou")
    return
  
  def andar(self):
    print(f"O veiculo {self.nome} andou.")
    return 

carro = Carro("Ferrari")
carro.ligar()
carro.andar()
carro.desligar()

# if I don't implement the mandatory methods defined in the abstract class,
# my program will return an error "requesting" them

#---> 23 carro = Carro("Ferrari")
#     24 '''carro.ligar()
#     25 carro.desligar()'''
#
#TypeError: Can't instantiate abstract class Carro with abstract methods desligar, ligar