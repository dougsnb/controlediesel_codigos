from dados_abastecimento import DadosAbastecimento
from calculadora_abastecimento import CalculadoraAbastecimento

class SistemaAbastecimento:
    def __init__(self):
        self.dados = DadosAbastecimento()
        self.calculadora = CalculadoraAbastecimento()

    def registrar_abastecimento(self, bomba_inicial, bomba_final, visor_final, recebimento, media_consumo):
        if self.dados.ultima_bomba_final is not None and bomba_inicial != self.dados.ultima_bomba_final:
            print(f"Aviso: diferença entre a bomba final do dia anterior ({self.dados.ultima_bomba_final}) e a inicial do dia atual ({bomba_inicial})")

        consumo_dia = self.calculadora.calcular_consumo_dia(bomba_inicial, bomba_final)
        print(f"Consumo do dia: {consumo_dia} litros")

        saldo_pos_abastecimento = self.calculadora.calcular_saldo_pos_abastecimento(self.dados.quantidade_no_tanque, consumo_dia)
        print(f"Saldo do tanque após abastecimento: {saldo_pos_abastecimento:.2f} litros")

        diferenca_visor = self.calculadora.calcular_diferenca_visor(saldo_pos_abastecimento, visor_final)
        print(f"Diferença entre o saldo do tanque e o visor: {diferenca_visor:.2f} litros")

        if not self.calculadora.verificar_capacidade_tanque(saldo_pos_abastecimento, recebimento, media_consumo):
            print(f"Aviso: O tanque não terá capacidade para receber o diesel do próximo dia.")
        else:
            print(f"O tanque terá capacidade para receber o diesel do próximo dia.")

        self.dados.quantidade_no_tanque = saldo_pos_abastecimento + recebimento

        self.dados.ultima_bomba_final = bomba_final

        self.dados.salvar_dados()
