idade = int(input("Digite sua idade: "))
dinheiro = int(input("Quanto dinheiro você tem: "))
carteira = input("Você tem carteira? (Y/N) ")

if(idade>= 18 and dinheiro>= 50) or carteira == "Y":
    print("Você pode alugar o carro!")
else:
    print("Você não pode alugar o carro!")