import time
import os

class ContaBancaria:
    MAX_SAQUE = 3 #Limite maximo de saque em um dia

    def __init__(self):
        self.histórico_conta = []
        self.dados_conta = {"saldo": 0.0}
        self.num_saques = 0

    def sair(self):
        print("Transações encerradas!")
        print("Saindo ...")

    def deposito(self):
        
        self.interface("Depósito")

        try:
            print("Exemplo de entrada 1.0")
            valor_deposito = float(input("Digite o valor de depósito desejado: "))

            valor_deposito = valor_deposito*100

            if valor_deposito > 0:
                self.dados_conta["saldo"] += valor_deposito
                self.interface("Depósito realizado com sucesso!")
                self.saldo()
                self.histórico_conta.append(f"Depósito de R${valor_deposito / 100:.2f}")

                time.sleep(5)
                self.clear_console()

            else:
                print("O valor do depósito deve ser maior que zero.")

        except ValueError:
            print("Por favor, digite um valor numérico válido.")
            print("Por exemplo: 15.00")
            time.sleep(3)

    def saque(self):
        self.interface("Saque")
        self.saldo()

        if self.dados_conta["saldo"] <= 0:
            print("Saldo da conta insuficiente para saque.")
        elif self.num_saques >= self.MAX_SAQUE:
            print(f"Você atingiu o limite máximo de {self.MAX_SAQUE} saques por dia.")
        else:
            valor_maximo_saque = min(500, self.dados_conta["saldo"] / 100)
            print(f"Valor máximo de saque: R${valor_maximo_saque:.2f}")

            try:
                print("Exemplo de entrada 1.0")
                valor_saque = float(input("Digite o valor do saque: "))
                valor_saque = int(valor_saque * 100)  # Converte para centavos

                if 0.0 < valor_saque <= valor_maximo_saque*100:
                    self.dados_conta["saldo"] -= valor_saque
                    print(f"\nSaque de R${valor_saque / 100:.2f} realizado com sucesso!")
                    self.num_saques += 1  # Aumenta o contador de saques
                    self.histórico_conta.append(f"Saque de R${valor_saque / 100:.2f}")

                else:
                    print("\nValor de saque inválido.")

            except ValueError:
                print("Por favor, digite um valor numérico válido.")
                time.sleep(3)

        self.saldo()
        time.sleep(5)
        self.clear_console()

    def extrato(self):
        self.interface("Extrato")
        self.saldo()
        # Verifica se existe algum histórico de transações antes de tentar iterar sobre ele
        if len(self.histórico_conta) > 0:
            self.interface("Histórico de Movimentação da conta")
            for item in self.histórico_conta:
                print(item)
            time.sleep(5)
        else:
            print("Nenhuma transação no histórico.")

    def saldo(self):
        print("Saldo atual: R${:.2f}".format(self.dados_conta["saldo"] / 100))

    def interface(self, mensagem):
        print("-----------------------------------------------------------")
        print("             ", mensagem)

    def clear_console(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    # Mapeamento das operações para os métodos da classe
    operacoes = {
        "0": "sair",
        "1": "deposito",
        "2": "saque",
        "3": "extrato"
    }
