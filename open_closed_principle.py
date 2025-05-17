# open_closed_principle.py

from abc import ABC, abstractmethod

# Classe Pedido reutilizável
class Pedido:
  """
  Representa um pedido feito por um cliente, com status atual.
  """
  def __init__(self, cliente: str, total: float):
    self.cliente = cliente
    self.total = total
    self.status = "pendente"

  def atualizar_status(self, novo_status: str):
    """
    Atualiza o status do pedido.
    """
    self.status = novo_status
    print(f"Status do pedido de {self.cliente} atualizado para: {self.status}")


# Interface abstrata para processadores de pagamento
class ProcessadorDePagamento(ABC):
  """
  Interface base para qualquer forma de processador de pagamento.
  """
  @abstractmethod
  def processar(self, pedido: Pedido):
    pass


# Implementação específica para cartão
class ProcessadorDeCartao(ProcessadorDePagamento):
  def processar(self, pedido: Pedido):
    print(f"Processando pagamento por cartão de {pedido.total} para {pedido.cliente}...")
    pedido.atualizar_status("pago")


# Implementação específica para boleto
class ProcessadorDeBoleto(ProcessadorDePagamento):
  def processar(self, pedido: Pedido):
    print(f"Processando pagamento por boleto de {pedido.total} para {pedido.cliente}...")
    pedido.atualizar_status("pago")


# Simulando um notificador (ex: por email)
class Notificador:
  def notificar(self, pedido: Pedido):
    print(f"Enviando notificação: Pedido de {pedido.cliente} está com status '{pedido.status}'.")


# Uso do sistema — pronto para extensão sem alteração
if __name__ == "__main__":
  notificador = Notificador()

  # Pedido com cartão
  pedido = Pedido("Maria", 200.00)
  processador_cartao = ProcessadorDeCartao()
  processador_cartao.processar(pedido)
  notificador.notificar(pedido)

  print()  # Separador

  # Pedido com boleto
  pedido_boleto = Pedido("Carlos", 300.00)
  processador_boleto = ProcessadorDeBoleto()
  processador_boleto.processar(pedido_boleto)
  notificador.notificar(pedido_boleto)
