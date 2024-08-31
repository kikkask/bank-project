from datetime import datetime
saldo = 0
limite = 500.00
extrato = "=============EXTRATO=============\n"
numero_saques = 0
limite_saques = 3
transacoes = 0
limite_transac = 10

while True:
    menu = f'''
Bem-vindo ao SJC Bank!
Seu saldo atual é de R$ {saldo:.2f}
Por favor, digite um comando para realizar uma operação:
[d] Depósito
[s] Saque
[e] Extrato
[o] Sair

-->'''

    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))
        if transacoes >= limite_transac:
            print("Operação Inválida, você já atingiu seu limite de operações bancárias hoje.")
        elif valor >= 0:
            saldo += valor
            date_dep = datetime.today()
            if date_dep.strftime("%Y/%m/%d") == datetime.today().strftime("%Y/%m/%d"):
                transacoes += 1
            extrato += f"Depósito no valor de: {valor:.2f} às {date_dep}\n"
            print(f"Depósito no valor de R$ {valor:.2F} realizado com sucesso.")
        else:
            print("Operação falhou. Você não pode depositar um valor negativo.")
    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))
        if transacoes >= limite_transac:
            print("Operação Inválida, você já atingiu seu limite de operações bancárias hoje.")
        elif valor > saldo:
            print("Operação falhou. Você não tem saldo suficiente para realizar esse saque.")
        elif numero_saques >= limite_saques:
            print("Operação falhou, você já realizou todos os saques possíveis para hoje.")
        elif valor > limite:
            print("Operação falhou, seu limite é de R$ 500,00 por saque.")
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            date_saq = datetime.today()
            if date_saq.strftime("%Y/%m/%d") == datetime.today().strftime("%Y/%m/%d"):
                transacoes += 1
            extrato += f"Saque no valor de: {valor:.2f} às {date_saq}\n"
            print(f"Saque no valor de R$ {valor:.2F} realizado com sucesso.")
        else:
            print("Operação falhou, quantidade inválida.")
    elif opcao == "e":
        print(extrato)
    elif opcao == "o":
        print("O SJC Bank agradece seu acesso. Até a próxima :)")
        break
    else:
        print("Por favor digite um comando válido para realizar uma operação")