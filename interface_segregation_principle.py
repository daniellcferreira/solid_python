from abc import ABC, abstractmethod

# Exemplo de classe Pedido simples
class Pedido:
  """
  Representa um pedido feito por um cliente.
  """
  def __init__(self, cliente: str, status: str):
    self.cliente = cliente
    self.status = status


# Interface base para notificadores
class Notificador(ABC):
  """
  Interface para notificadores.
  Força implementação apenas do método necessário.
  """
  @abstractmethod
  def notificar(self, pedido: Pedido):
    pass


# Implementação específica para notificação por email
class NotificadorEmail(Notificador):
  def notificar(self, pedido: Pedido):
    print(f"Enviando email para {pedido.cliente}: Seu pedido foi {pedido.status}.")


# Implementação específica para notificação por SMS
class NotificadorSMS(Notificador):
  def notificar(self, pedido: Pedido):
    print(f"Enviando SMS para {pedido.cliente}: Seu pedido foi {pedido.status}.")


# Exemplo de uso
if __name__ == "__main__":
  # Criando pedidos fictícios
  pedido_cartao = Pedido("Maria", "aprovado")
  pedido_boleto = Pedido("Carlos", "pendente")

  # Instanciando notificadores
  notificador_email = NotificadorEmail()
  notificador_sms = NotificadorSMS()

  # Usando notificadores de forma independente (respeitando o ISP)
  notificador_email.notificar(pedido_cartao)
  notificador_sms.notificar(pedido_boleto)
