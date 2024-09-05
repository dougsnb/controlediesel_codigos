import json
import os

class DadosAbastecimento:
    def __init__(self, arquivo_dados='dados_abastecimento.json'):
        self.arquivo_dados = arquivo_dados
        self.quantidade_no_tanque = 0
        self.ultima_bomba_final = None
        self.carregar_dados()

    def carregar_dados(self):
        """Carregar dados do arquivo JSON, se existir."""
        if os.path.exists(self.arquivo_dados):
            with open(self.arquivo_dados, 'r') as f:
                dados = json.load(f)
                self.quantidade_no_tanque = dados.get('quantidade_no_tanque', 0)
                self.ultima_bomba_final = dados.get('ultima_bomba_final')
        else:
            self.salvar_dados()

    def salvar_dados(self):
        """Salvar os dados no arquivo JSON."""
        dados = {
            'quantidade_no_tanque': self.quantidade_no_tanque,
            'ultima_bomba_final': self.ultima_bomba_final
        }
        with open(self.arquivo_dados, 'w') as f:
            json.dump(dados, f)

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

class SistemaAbastecimento:
    def __init__(self):
        self.dados = DadosAbastecimento()
        self.calculadora = CalculadoraAbastecimento()

    def registrar_abastecimento(self, bomba_inicial, bomba_final, visor_final, recebimento, media_consumo):
        
        if self.dados.ultima_bomba_final is not None and bomba_inicial != self.dados.ultima_bomba_final:
            print("\nRESUMO DO DIA")
            print(f"\nAviso: diferença entre a bomba final do dia anterior ({self.dados.ultima_bomba_final}) e a inicial do dia atual ({bomba_inicial})")

        consumo_dia = self.calculadora.calcular_consumo_dia(bomba_inicial, bomba_final)
        print(f"\nConsumo do dia: {consumo_dia} litros")

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

def main():
    sistema = SistemaAbastecimento()

    quantidade_inicial_tanque = float(input("Informe quantidade de diesel inicial do sistema: "))
    sistema.dados.quantidade_no_tanque = quantidade_inicial_tanque

    bomba_inicial = float(input("Informe o número da bomba inicial: "))

    while True:
        bomba_final = float(input("Informe o número da bomba final: "))
        visor_final = float(input("Informe o número do visor: "))
        recebimento = float(input("Informe o recebimento de diesel do dia seguinte: "))
        media_consumo = float(input("Informe a média de consumo de diesel para o próximo dia:"))

        sistema.registrar_abastecimento(bomba_inicial, bomba_final, visor_final, recebimento, media_consumo)

        continuar = input("Deseja continuar (s/n)? ").lower()
        if continuar != 's':
            break
        else:
            bomba_inicial = sistema.dados.ultima_bomba_final
            print(f"Bomba inicial automaticamente definida como: {bomba_inicial}")

if __name__ == "__main__":
    main()
