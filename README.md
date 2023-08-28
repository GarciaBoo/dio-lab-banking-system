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
Criar usuário (Cliente do Banco)                  [ ]
Criar Conta Corrente (vinculado com usuário)      [ ]

## Depósito
A função deve receber argumontos apenas por posição (Positional Only)[ ]

## Saque
A função deve receber argumontos apenas por nome (Keyword Only)[ ]

## Extrato
Posicional Saldo.
Nomeados Extrato.

A função deve receber argumontos por nome (Keyword Only) e posição (Positional Only)[ ]

## Criar usuário (Cliente)
Armazenar usuários em uma lista [ ]
Usuário é composto por: nome, data de nascimento, cpf e endereço. [ ]
Endereço ser uma string com formato: logradouro, nro - bairro - cidade/sigla estado. [ ]
Armazenar somente os números do CPF. [ ]
Verifica se o cpf já está cadastrado [ ]

## Criar Conta Corrente
Armazenar contas em uma lista [ ]
Conta é composto por: agência, número da conta e usuário. [ ]
Número da Conta é sequencial, incia em 1 [ ]
Número da agência é fixo: 0001 [ ]
O úsuario pode ter mais de uma conta [ ]
Uma conta pode ter somente um usuário [ ]
