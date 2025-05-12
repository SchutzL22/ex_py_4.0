print(f"Insira valores reais ")
comecarpor = int(input("Insira o valor que quer começar: "))
terminarem = int(input("Insira o valor que quer terminar: "))
multi = int(input("Insira o múltiplo: "))
nmulti = 0
soma = 0

terminarem = terminarem + 1

for n in range(comecarpor, terminarem):
    nmulti = nmulti + n

    if n % multi == 0:
        soma = soma + n

print(f"A soma dos múltiplos de {multi}, do intervalo de {comecarpor} e {terminarem} é de: {soma}")