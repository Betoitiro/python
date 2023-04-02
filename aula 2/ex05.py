debito = float(input("digite seu capital em debito: "))
credito = float(input("digite seu capital em credito: "))
saldo = debito + credito
print(saldo)
if saldo > 0:
    print("saldo positivo!")
else:
    print("saldo negativo!")