from sistema_abastecimento import SistemaAbastecimento

def main():
    sistema = SistemaAbastecimento()

    quantidade_inicial_tanque = float(input("Informe a carga de diesel inicial no sistema: "))
    sistema.dados.quantidade_no_tanque = quantidade_inicial_tanque

    bomba_inicial = float(input("Informe o número da bomba inicial: "))

    while True:
        bomba_final = float(input("Informe o número da bomba final: "))
        visor_final = float(input("Informe o número do visor: "))
        recebimento = float(input("Informe o recebimento de diesel do dia seguinte: "))
        media_consumo = float(input("Informe a média de consumo de diesel para o próximo dia: "))

        sistema.registrar_abastecimento(bomba_inicial, bomba_final, visor_final, recebimento, media_consumo)

        continuar = input("Deseja continuar (s/n)? ").lower()
        if continuar != 's':
            break
        else:
            bomba_inicial = sistema.dados.ultima_bomba_final
            print(f"Bomba inicial automaticamente definida como: {bomba_inicial}")

if __name__ == "__main__":
    main()
