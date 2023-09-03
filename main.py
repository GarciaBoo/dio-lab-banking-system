import deposit
import time
3
def main():
    conta = deposit.ContaBancaria()  # Crie uma instância da classe ContaBancaria

    print("Olá!")
    print("Bem-vindo à sua conta bancária")

    while True:
        print("Menu de operações:")
        print("1: Depósito")
        print("2: Saque")
        print("3: Extrato")
        print("4: nova_conta")
        print("5: novo_usuário")
        print("6: listar_usuarios")
        print("7: listar_contas")
        print("0: Sair")

        opt = input("Digite o número da operação a ser realizada: ")

        if opt in conta.operacoes:
            conta.clear_console()
            operacao = conta.operacoes[opt]  # Obtenha o nome do método com base na escolha
            getattr(conta, operacao)()  # Chame o método correspondente da instância conta
            time.sleep(2)
            conta.clear_console()
        else:
            conta.clear_console()
            print("Operação inválida!")
            print("Tente escolher uma opção válida.")
            print("Por exemplo, para Depósito, digite: 1")
            conta.clear_console()

        if opt == "0":
            break

if __name__ == "__main__":
    main()
