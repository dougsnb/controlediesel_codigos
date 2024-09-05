class CalculadoraAbastecimento:
    def __init__(self, capacidade_tanque=15000):
        self.capacidade_tanque = capacidade_tanque

    def calcular_consumo_dia(self, bomba_inicial, bomba_final):
        """Calcular o consumo do dia."""
        return bomba_final - bomba_inicial

    def calcular_saldo_pos_abastecimento(self, quantidade_no_tanque, consumo_dia):
        """Calcular o saldo do tanque após abastecimento."""
        return quantidade_no_tanque - consumo_dia

    def calcular_diferenca_visor(self, saldo_pos_abastecimento, visor_final):
        """Calcular a diferença entre o saldo do tanque e o visor."""
        return saldo_pos_abastecimento - visor_final

    def verificar_capacidade_tanque(self, saldo_pos_abastecimento, recebimento, media_consumo):
        """Verificar se o tanque terá capacidade para o recebimento no próximo dia."""
        capacidade_restante = saldo_pos_abastecimento + recebimento - media_consumo
        return capacidade_restante <= self.capacidade_tanque
