import time
import os

class ContaBancaria:
    MAX_SAQUE = 3 #Limite maximo de saque em um dia
    AGENCIA = "0001" #Número da agência é fixo: 0001

    def __init__(self):
        self.historico_conta = []
        self.dados_conta = {"saldo": 0.0}
        self.num_saques = 0
        self.usuarios = []
        self.contas = []

    def sair(self):
        print("Transações encerradas!")
        print("Saindo ...")

    def depositar(self, saldo, valor, /): #Realiza a operação do depósito
        if valor> 0:
            saldo += valor
            self.interface(f"Depósito de R${valor / 100:.2f} realizado com sucesso!")
            self.historico_conta.append(f"Depósito de R${valor / 100:.2f}")
            time.sleep(5)
            self.clear_console()
        else:
            print("O valor do depósito deve ser maior que R$0.00")
        
        return saldo

    def deposito(self):
        self.interface("Depósito")
        try:
            print("Exemplo de entrada 1.0")
            valor = float(input("Digite o valor de depósito desejado: "))
            valor = valor*100
            self.dados_conta["saldo"] = self.depositar(self.dados_conta["saldo"], valor)

        except ValueError:
            print("Por favor, digite um valor numérico válido.")
            print("Por exemplo: 15.00")
            time.sleep(3)

    def sacar(self, *, saldo, valor, limite_saques): #Realiza a operação do saque
        if 0.0 < valor <= limite_saques*100:
            saldo -= valor
            print(f"\nSaque de R${valor / 100:.2f} realizado com sucesso!")
            self.num_saques += 1  # Aumenta o contador de saques
            self.historico_conta.append(f"Saque de R${valor / 100:.2f}")
        else:
            print(f"\nSaldo de saque invalido, tente um valor entre R$0.0 e R${saldo / 100:.2f}.")
        return  saldo
    
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
                valor = float(input("Digite o valor do saque: "))
                valor = int(valor * 100)  # Converte para centavos

                self.dados_conta["saldo"] = self.sacar(saldo = self.dados_conta["saldo"], valor = valor, limite_saques = valor_maximo_saque)

            except ValueError:
                print("Por favor, digite um valor numérico válido.")
                time.sleep(3)

        self.saldo()
        time.sleep(5)
        self.clear_console()

    def imprime_extrato(self, saldo, /, *, historico):
        print("Saldo atual: R${:.2f}".format(saldo / 100))
        if len(historico) > 0:   # Verifica se existe algum histórico de transações antes de tentar iterar sobre ele
            self.interface("Histórico de Movimentação da conta")
            for item in historico:
                print(item)    
            time.sleep(5)
        else:
            print("Não foram realizadas movimentações.")

    def extrato(self):
        self.interface("Extrato")
        # Chamada para crumprir requisito do desafio
        # A função deve receber argumentos por nome (Keyword Only) e posição (Positional Only)
        self.imprime_extrato(self.dados_conta["saldo"] / 100, historico = self.historico_conta)

    def saldo(self):
        print("Saldo atual: R${:.2f}".format(self.dados_conta["saldo"] / 100))

    def interface(self, mensagem): #imprime uma mensagem para ajustar a interface no console
        print("-----------------------------------------------------------")
        print("             ", mensagem)

    def clear_console(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def nova_conta(self):
        self.interface("Criar uma Conta")
        numero_conta = len(self.contas) + 1
        conta = self.criar_conta(self.AGENCIA, numero_conta, self.usuarios)

        if conta:
            self.contas.append(conta)

    def criar_conta(self, agencia, numero_conta, user_list):
        cpf = input("Informe o cpf do usuario: ")
        usuario = self.filtrar_usuario(cpf, user_list)

        if usuario:
            print("Conta criada com sucesso!")
            return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

        print ("Usuário não encontrado, criação de conta cancelada.")
        return None
        
    
    def novo_usuário(self):
        self.interface("Cadastrar Usuário")
        cpf = input("Informe o CPF (somente o número): ")
        usuario = self.filtrar_usuario(cpf,self.usuarios)
        
        if usuario:
            print("Usuário já cadastrado!")
            return
        
        nome = input("Informe o nome completo: ")
        data_nascimento = input("informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        self.usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

        print("--------------- Usuário criado com sucesso! --------------------")
    
    def filtrar_usuario(self, cpf, user_list):
        usuarios_filtrados = [usuario for usuario in  user_list if usuario["cpf"] == cpf]
        return usuarios_filtrados[0] if usuarios_filtrados else None

    def listar_usuarios(self):
        self.interface("Lista de Usuários por CPF cadastrado")
        if len(self.usuarios) > 0:   # Verifica se existe algum histórico de transações antes de tentar iterar sobre ele
            for item in self.usuarios:
                print(item["cpf"])    
            time.sleep(5)
        else:
            print("Não existe usuários cadastrados.")

    def listar_contas(self):
        self.interface("Lista de Contas")
        if len(self.contas) > 0:
            for conta in self.contas:
                print(f"Agência: {conta['agencia']}")
                print(f"C/C: {conta['numero_conta']}")
                print(f"Titular: {conta['usuario']['nome']}")
                print("=" * 100)
            time.sleep(5)
        else:
            print("Não existem contas cadastradas.")


    # Mapeamento das operações para os métodos da classe
    operacoes = {
        "0": "sair",
        "1": "deposito",
        "2": "saque",
        "3": "extrato",
        "4": "nova_conta",
        "5": "novo_usuário",
        "6": "listar_usuarios",
        "7": "listar_contas"
    }
