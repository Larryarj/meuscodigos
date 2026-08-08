def adicionarItem(dicionario, item , qtd):

    if item in dicionario.keys():

        dicionario[item] += qtd
        print(f'você já tem esse item no inventário, quantidade atualizada para {dicionario[item]}')

    else:

        dicionario.update({item : qtd})
        print('item adicionado ao inventário.')

def mostrarInventario(dicionario):

    for chave, valor in dicionario.items():
        print(chave, valor)

def main():

    inventario = {

        'cura' : 3

    }

    while True:

        acao = int(input('qual ação deseja realizar? digite:\n'
                         '1 para ver os items do inventário;\n'
                         '2 para adicionar items ao inventário;\n'))
        
        match acao:

            case 1:
                mostrarInventario(inventario)

            case 2:
                ItemToAdd = input('digite qual item voce quer adicionar: ')
                ItemqtdToAdd = int(input('digite quantos serão adicionados: '))
                adicionarItem(inventario, ItemToAdd, ItemqtdToAdd)

            case _:
                break

main()
