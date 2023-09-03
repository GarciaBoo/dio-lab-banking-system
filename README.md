# dio-lab-Criando-um-sistema-bancário
## Desafio
Fomos contratados por um grande banco para desenvolver o
seu novo sistema. Esse banco deseja modernizar suas
operações e para isso escolheu a linguagem Python. Para a
primeira versão do sistema devemos implementar apenas 3
operações: depósito, saque e extrato.

## Depósito
Deve ser possível depositar valores positivos para a minha
conta bancária. A v1 do projeto trabalha apenas com 1 usuário,
dessa forma não precisamos nos preocupar em identificar qual
é o número da agência e conta bancária. Todos os depósitos
devem ser armazenados em uma variável e exibidos na
operação de extrato.

## Saque
O sistema deve permitir realizar 3 saques diários com limite
máximo de R$ 500,00 por saque. Caso o usuário não tenha
saldo em conta, o sistema deve exibir uma mensagem
informando que não será possível sacar o dinheiro por falta de
saldo. Todos os saques devem ser armazenados em uma
variável e exibidos na operação de extrato.

## Extrato
Essa operação deve listar todos os depósitos e saques
realizados na conta. No fim da listagem deve ser exibido o
saldo atual da conta. Se o extrato estiver em branco, exibir a
mensagem: Não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx,
exemplo:
1500.45 = R$ 1500.45

# Versão 2 do Desafio
## Altereções feitas.
Modularizar em funções saque, deposito e extrato. [X]
Criar usuário (Cliente do Banco)                  [X]
Criar Conta Corrente (vinculado com usuário)      [X]
 Opcional Listar Usuário                          [X]

 
## Depósito
A função deve receber argumentos apenas por posição (Positional Only) [X]

## Saque
A função deve receber argumentos apenas por nome (Keyword Only) [X]

## Extrato
A função deve receber argumentos por nome (Keyword Only) e posição (Positional Only) [X]

## Criar usuário (Cliente)
Armazenar usuários em uma lista [X]
Usuário é composto por: nome, data de nascimento, cpf e endereço. [X]
Endereço ser uma string com formato: logradouro, nro - bairro - cidade/sigla estado. [X]
Armazenar somente os números do CPF. [X]
Verifica se o cpf já está cadastrado [X]

## Criar Conta Corrente
Armazenar contas em uma lista [X]
Conta é composto por: agência, número da conta e usuário. [X]
Número da Conta é sequencial, incia em 1 [X]
Número da agência é fixo: 0001 [x]
O úsuario pode ter mais de uma conta [X]
Uma conta pode ter somente um usuário [X]
