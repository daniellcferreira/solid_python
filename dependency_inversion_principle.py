from single_responsability_principle import Pedido, Usuario

# Interface abstrata para processadores de pagamento
class ProcessadorDePagamento:
  """
  Define a interface para qualquer tipo de processador de pagamento.
  """
  def processar(self, pedido: Pedido):
    raise NotImplementedError("Este método deve ser implementado por subclasses.")


# Implementação concreta de pagamento via cartão
class ProcessadorCartao(ProcessadorDePagamento):
  def processar(self, pedido: Pedido):
    print(f"Processando pagamento com cartão para {pedido.usuario.nome}.")


# Implementação concreta de pagamento via boleto
class ProcessadorBoleto(ProcessadorDePagamento):
  def processar(self, pedido: Pedido):
    print(f"Processando pagamento com boleto para {pedido.usuario.nome}.")


class SistemaDePedidos:
  """
  Módulo de alto nível que depende de uma abstração (interface de pagamento),
  e não de implementações concretas diretamente.
  """

  def __init__(self, processador: ProcessadorDePagamento):
    # Injeção da dependência via construtor (injeção de dependência)
    self.processador = processador

  def realizar_pedido(self, usuario: Usuario, total: float):
    """
    Cria um novo pedido e utiliza o processador injetado para processar o pagamento.
    """
    pedido = Pedido(usuario, total)
    self.processador.processar(pedido)


# Exemplo de uso
if __name__ == "__main__":
  usuario = Usuario("Pedro", "pedro@example.com")

  # Injetando um processador de cartão no sistema
  sistema_cartao = SistemaDePedidos(ProcessadorCartao())
  sistema_cartao.realizar_pedido(usuario, 300.00)

  # Injetando um processador de boleto no sistema
  sistema_boleto = SistemaDePedidos(ProcessadorBoleto())
  sistema_boleto.realizar_pedido(usuario, 150.00)
