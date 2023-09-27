def clean():
    print('\n' * 10)
clean()
print('Supermercado')
valor = int(input('Digite o valor do produto: '))
desc = int(input('Quantos de desconto irá receber? '))
clean()
valor_final = (desc / 100 )* valor
print('o valor será',valor - valor_final)