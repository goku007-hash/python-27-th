def clean():
    print('\n'*10)
clean()
def calcular_notas(valor):
    notas_de_50 = valor // 50
    valor_restante = valor % 50
    notas_de_10 = valor_restante // 10
    notas_de_1 = valor_restante // 1
    return notas_de_50, notas_de_10, notas_de_1
valor_desejado = int(input("Digite o valor desejado: "))
clean()

notas_de_50, notas_de_10,notas_de_1= calcular_notas(valor_desejado)

print(f"Notas de 50: {notas_de_50}")
print(f"Notas de 10: {notas_de_10}")
print(f"Notas de 10: {notas_de_1}")