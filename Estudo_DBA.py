import pandas as pd

pd.Series(data=5)
lista_nomes = 'Rerisson Henrique Rodrigues Silva'.split()
pd.Series(lista_nomes)
dados = {
    'nome1': 'Rerisson',
    'nome2': 'Henrique',
    'nome3': 'Rodrigues',
    'nome4': 'Silva',
}
pd.Series(dados)

cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()

pd.Series(lista_nomes, index=cpfs)