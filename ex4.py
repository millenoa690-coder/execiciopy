def atualizar_saldo(saldo, valor, operacao):
    if operacao == "deposito":
        saldo = saldo + valor
    elif operacao == "saque":
        saldo = saldo - valor
    return saldo