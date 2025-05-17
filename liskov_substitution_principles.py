from abc import ABC, abstractmethod


# Classe base abstrata para qualquer tipo de entrega
class Entrega(ABC):
  """
  Classe abstrata que define a interface para tipos de entrega.
  Todas as subclasses devem implementar o método calcular_tempo().
  """

  @abstractmethod
  def calcular_tempo(self) -> str:
    """
    Deve retornar uma string indicando o tempo de entrega.
    """
    pass


# Subclasse para entrega expressa
class EntregaExpressa(Entrega):
  def calcular_tempo(self) -> str:
    return "Entrega em 1 dia"


# Subclasse para entrega normal
class EntregaNormal(Entrega):
  def calcular_tempo(self) -> str:
    return "Entrega em 5 dias"


def verificar_entrega(entrega: Entrega):
  """
  Função genérica que aceita qualquer tipo de entrega
  e exibe o tempo calculado — aplica o princípio de substituição de Liskov.
  """
  print(f"Tempo de entrega: {entrega.calcular_tempo()}")


# Exemplo de uso
if __name__ == "__main__":
  entrega_expressa = EntregaExpressa()
  entrega_normal = EntregaNormal()

  verificar_entrega(entrega_expressa)  # Substituição válida
  verificar_entrega(entrega_normal)    # Substituição válida