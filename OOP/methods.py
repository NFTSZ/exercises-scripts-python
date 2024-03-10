# Decoradores comuns: @classmethod e @staticmethod 
# O classmethod é utilizado para criar instâncias a partir de configurações 
# globais, enquanto o staticmethod é utilizado para executar funções específicas
# sem acesso aos atributos da instância ou da classe

class MinhaClase:
  valor = 10 # atributo da classe

  def __init__(self, nome) -> None:
    self.nome = nome  # atributo da instancia

  # requer uma instancia pra ser chamado
  def metodo_instancia(self):
    return f"Metodo de instancia chamado para {self.nome}"

  @classmethod
  def metodo_classe(cls):
    return f"Metodo de classe chamado para valor={cls.valor}"

  @staticmethod
  def metodo_estatico():
    return "Metodo estatico chamado."

objeto = MinhaClase("Exemplo")
print(objeto.metodo_instancia())
print(MinhaClase.valor)
print(MinhaClase.metodo_classe())
print(MinhaClase.metodo_estatico())

# classmethod Example
class Carro:
  def __init__(self, marca, modelo, ano) -> None:
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

  @classmethod
  def criar_carro(cls, configuracao):
    marca, modelo, ano = configuracao.split(',')
    return cls(marca, modelo, int(ano))

configuaraco1 = "Toyota,Corolla,2022"
carro = Carro.criar_carro(configuaraco1)
print(f"Marca: {carro.marca}\nModelo: {carro.modelo}\nAno: {carro.ano}")


# staticmethod Example
class Matematica:
  @staticmethod
  def somar(a, b):
    return a + b

print(Matematica.somar(2, 2))