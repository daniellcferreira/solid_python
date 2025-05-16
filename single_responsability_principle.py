from enum import Enum

# Enum para representar os possíveis status de um pedido
class StatusPedido(Enum):
  PENDENTE = "pendente"
  PAGO = "pago"
  ENVIADO = "enviado"


class Usuario:
  """
  Representa um usuário com nome e email.
  Responsável apenas por armazenar e gerenciar os dados do usuário.
  """

  def __init__(self, nome: str, email: str):
    self.nome = nome
    self.email = email

  def atualizar_email(self, novo_email: str):
    """
    Atualiza o email do usuário.
    """
    self.email = novo_email

  def __str__(self):
    """
    Retorna uma representação textual do usuário.
    """
    return f"{self.nome} ({self.email})"


class Pedido:
  """
  Representa um pedido realizado por um usuário.
  Responsável apenas por dados e ações relacionadas ao pedido.
  """

  def __init__(self, usuario: Usuario, total: float):
    self.usuario = usuario
    self.total = total
    self.status = StatusPedido.PENDENTE  # Status inicial do pedido

  def atualizar_status(self, status: StatusPedido):
    """
    Atualiza o status do pedido.
    """
    self.status = status

  def confirmar_pagamento(self, notificador):
    """
    Confirma o pagamento do pedido e notifica o usuário.
    Aplica injeção de dependência com o notificador.
    """
    self.atualizar_status(StatusPedido.PAGO)
    notificador.notificar(self.usuario, "Seu pedido foi pago com sucesso!")

  def __str__(self):
    """
    Retorna uma descrição textual do pedido.
    """
    return f"Pedido de {self.usuario} - Total: R${self.total:.2f} - Status: {self.status.value}"


class Notificador:
  """
  Responsável por enviar notificações ao usuário.
  """

  def notificar(self, usuario: Usuario, mensagem: str):
    """
    Simula o envio de uma notificação para o usuário.
    Aqui poderíamos integrar com email, SMS, etc.
    """
    print(f"[NOTIFICAÇÃO] Para {usuario.nome}: {mensagem}")


# Exemplo de uso das classes acima
if __name__ == "__main__":
  # Cria um usuário e um pedido associado
  usuario = Usuario("João", "joao@example.com")
  pedido = Pedido(usuario, 150.00)
  notificador = Notificador()

  # Confirma o pagamento do pedido e envia uma notificação
  pedido.confirmar_pagamento(notificador)
