# Encapsulation
# Involves the use of private attributes and methods 
# to protect sensitive information and ensure data integrity

class ContaBancaria:
  def __init__(self, saldo):
    self.__saldo = saldo  # private method
  
  def depositar(self, valor):
    if valor > 0:
      self.__saldo += valor

  def sacar(self, valor):
    if valor > 0 and valor <= self.__saldo:
      self.__saldo -= valor

  def consultarSaldo(self):
    return self.__saldo

conta = ContaBancaria(1000)
print(f" Sua conta possui {conta.consultarSaldo()} de saldo.")
conta.depositar(500)
print(f" Sua conta possui {conta.consultarSaldo()} de saldo.")
conta.sacar(275)
print(f" Sua conta possui {conta.consultarSaldo()} de saldo.")
