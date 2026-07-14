# uma empresa prcisa registrar as informações dos seus funcionários:
# -departamento (TI, financeiro, RH, gestão);
# -salário (em R$);
# -nome;
# -cpf (123.456.678.10);
# -data de nascimento.
# o sisstema deve armazenar um funcionário por linha de uma matriz.
# o sistema deve:
# -consultar dados de funcionário por nome;
# -consultar dados de funcionário por cpf;
# -mostrar foncionarios por departamento (ex:todos funcionários de TI)
# -adicionar novos funcionários,sem permitir dados invalidos
# -alterar e remover funcionarios por cpf

bancodados = [[],
              [],
              [],
              [],
              []]

print('bem vindo ao sistema de registro!')

# função de consulta por nome:

def consulta_por_nome(bancodedados):
    
    nome_para_cosultar = input('qual o nome do funcionário que voce quer consultar? ') 
            
    if nome_para_cosultar in bancodados[2]: # verificar se o nome informado existe no banco de dados (na linha de nomes)
                
        print('funcionário encontrado!')
                
        nome_funcionário_index = bancodados[2].index(nome_para_cosultar) # descobrir e armazenar indice do nome informado

        print('departamento: ' , bancodados[0][nome_funcionário_index]) # imprimindo departamento no mesmo indice(coluna) do nome informado
        print('salário do funcionário: ' , bancodados[1][nome_funcionário_index]) # imprimindo salário no mesmo indice(coluna) do nome informado
        print('nome do funcionário: ' , bancodados[2][nome_funcionário_index]) # imprimindo nome no mesmo indice(coluna) do nome informado
        print('cpf do funcionário: ' , bancodados[3][nome_funcionário_index]) # imprimindo cpf no mesmo indice(coluna) do nome informado
        print('data de nascimento do funcionário; ' , bancodados[4][nome_funcionário_index]) # imprimindo data de nascimento no mesmo indice(coluna) do nome informado

    else:
        print('funcionário não encontrado!')

# função de consulta por cpf

def consulta_por_cpf(bancodedados):

    cpf_para_consultar = input('qual cpf voce quer consultar? ')

    if cpf_para_consultar in bancodados[3]: # verificar se o cpf informado existe no banco de dados(na linha de cpf)

        print('funcionário encontrado!')

        cpf_funcionario_index = bancodados[3].index(cpf_para_consultar) # descobrir e armazenar indice do cpf informado

        print('departamento: ' ,  bancodados[0][cpf_funcionario_index]) # imprimindo departamento no mesmo indice(coluna) do cpf informado
        print('salário do funcionário: ' , bancodados[1][cpf_funcionario_index]) # imprimindo salario no mesmo indice(coluna) do cpf informado
        print('nome do funcionário: ' , bancodados[2][cpf_funcionario_index]) # imprimindo nome no mesmo indice(coluna) do cpf informado
        print('cpf do funcionário: ' , bancodados[3][cpf_funcionario_index]) # imprimindo cpf no mesmo indice(coluna) do cpf informado
        print('data de nascimento do funcionário: ' , bancodados[4][cpf_funcionario_index]) # imprimindo data de nascimento no mesmo indice(coluna) do cpf informado

    else:
        print('cpf não encontrado!')

# funçao de mostrar funcionarios por departamento

def consulta_por_departamento(bancodedados):

    departamento_para_consultar = input('qual departamento voce quer consultar? digite: "TI, financeiro, RH ou gestao": ')

    if departamento_para_consultar == 'TI' or departamento_para_consultar == 'financeiro' or departamento_para_consultar == 'RH' or departamento_para_consultar == 'gestao' : #verificando se o departamento informado existe
        
        if departamento_para_consultar in bancodados[0]:#correção: checar se existe alguém no departamento para poder imprimir
            
            for tipo_departamento in range( 0 , len(bancodados[0]) , 1): # esse for camina por toda a linha de departamentos(na matriz)...
                
                if bancodados[0][tipo_departamento] == departamento_para_consultar: # verifica se o departamento pelo qual o for está caminhando atualmente é igual ao informado...
                    
                    print('funcionários: ' , bancodados[2][tipo_departamento]) # caso sim, é impresso o nome do funcionário correspondente ao departamento requisitado.

        else:
            print('o departamento não possui nenhum funcionário.')

    else:
        print('departamento inexistente, tente novamente.')

# função de adcionar funcionário

def adicionar_funcionário(bancodedados):

    registrandos = int(input('quantos funcionários voce quer registrar? '))

    for funcionario_novo in range(0 , registrandos , 1):
    
        while True:
            
            departamento = int(input('qual o departamento do funcionário?digite:\n' \
                                     '1 para TI;\n' \
                                     '2 para financeiro;\n' \
                                     '3 para RH;\n' \
                                     '4 para gestão.' ))

            match departamento:

                case 1:
                    print('TI')
                    bancodados[0].append('TI')
                    break

                case 2:
                    print('financeiro')
                    bancodados[0].append('financeiro')
                    break

                case 3:
                    print('RH')
                    bancodados[0].append('RH')
                    break

                case 4:
                    print('gestão')
                    bancodados[0].append('gestão')
                    break
                    
                case _:
                    print('digito inválido,tente novamente.')

        while True:

            salario = float(input('qual o salário do funcionário? '))

            if salario < 0:
                print('salário inexistente, tente novamente')
                continue

            else:
                bancodados[1].append (salario)
                break

        while True:

            nome = input('qual o nome do funcionário? ')

            if type(nome) == str:
                bancodados[2].append (nome)
                break

            else:
                print('nome inválido, tente novamente. ')

        while True:

            cpf = input('digite o cpf do funcionário. ')

            cpf_limpo = cpf.replace('.' , '').replace('-' , '')

            if cpf_limpo.isdigit and len(cpf_limpo) == 11:
                bancodados[3].append (cpf)
                break

            else:
                print('cpf inválido, tente novamente')

        while True:

            data_nascimento = input('qual a data de nascimento do funcionário? digite apenas os numeros! Exemplo: 05082010. ')

            if data_nascimento.isdigit and len(data_nascimento) == 8:
                bancodados[4].append (data_nascimento)
                break

            else:
                print('data de nascimento inválida, tente novamente')

    print('funcionário adicionado!')

# funçao para remover funcionário por cpf

def remover_por_cpf(bancodedados):
    
    cpf_do_funcionario_a_remover = input('qual o cpf do funcionário que voce deseja remover? ')
    
    if cpf_do_funcionario_a_remover in bancodados[3]: # verificando se o cpf informado está na matriz(na linha de cpf)
        
        cpf_funcionario_index = bancodados[3].index(cpf_do_funcionario_a_remover) # descobrindo e armazenando o índice do cpf na matriz(na linha de cpf)

        bancodados[0].pop(cpf_funcionario_index) # apagando departamento no mesmo indice(coluna) do cpf informado
        bancodados[1].pop(cpf_funcionario_index) # apagando salário no mesmo indice(coluna) do cpf informado
        bancodados[2].pop(cpf_funcionario_index) # apagando nome no mesmo indice(coluna) do cpf informado
        bancodados[3].pop(cpf_funcionario_index) # apagando cpf no mesmo indice(coluna) do cpf informado
        bancodados[4].pop(cpf_funcionario_index) # apagando data de nascimento no mesmo indice(coluna) do cpf informado

        print('funcionário removido do sistema!')

    else:
        print('cpf inexistente, tente novamente.')

# função de alterar informações pelo cpf

def alteracao_por_cpf(bancodedados):

    cpf_do_funcionario_para_alterar_informacoes = input('digite o CPF do funcionário que você quer alterar as informações: ')
    
    if cpf_do_funcionario_para_alterar_informacoes in bancodados[3]:

        print('funcionário encontrado!')
    
        cpf_do_funcionario_index = bancodados[3].index(cpf_do_funcionario_para_alterar_informacoes)
        
        informacao_para_atualizar = int(input('qual informação você quer atualizar?\n'
                                        '1 para alterar departamento;\n'
                                        '2 para alterar salário;\n'
                                        '3 para atualizar nome;\n'
                                        '4 para atualizar cpf;\n'
                                        '5 para atualizar data de nascimento.'))
        
        match informacao_para_atualizar:

            case 1:
                
                print('alteração de departamento!')

                departament_atualizado = input('qual o novo departamento desse funcionário? digite: TI, financeiro, RH ou gestao. ')
                
                bancodados[0].pop(cpf_do_funcionario_index)
                bancodados[0].inset(cpf_do_funcionario_index , departament_atualizado)

                print('informação atualizada!')

            case 2:

                print('atualização de salário!')

                salario_atualizado = input('qual o salário atualizado desse corno? ')

                bancodados[1].pop(cpf_do_funcionario_index)
                bancodados[1].insert(cpf_do_funcionario_index , salario_atualizado)

                print('informação atualizada!')

            case 3:

                print('atualização de nome!')

                nome_atualizado = input('qual o nome atualizado desse funcionário? ')

                bancodados[2].pop(cpf_do_funcionario_index)
                bancodados[2].insert(cpf_do_funcionario_index , nome_atualizado)

                print('informação atualizada')

            case 4:

                print('alteração de cpf!')

                cpf_atualizado = input('qual o cpf atualizado desse funcionário? ')
                
                bancodados[3].pop(cpf_do_funcionario_index)
                bancodados[3].insert(cpf_do_funcionario_index , cpf_atualizado)

                print('informação atualizada!')

            case 5:

                print('atualização de data de nascimento!')

                datadenascimento_atualizada = input('qual a data de nascimento atualizada do funcionário? ')

                bancodados[4].pop(cpf_do_funcionario_index)
                bancodados[4].insert(cpf_do_funcionario_index , datadenascimento_atualizada)

                print('informação atualizada!')

            case _:
                print('informação inexistente, tente novamente.')

    else:
        print('funcionário não encontrado, tente novamente.')   

# código para realizar ações no banco de dados

while True:

    acao = int(input('qual ação você quer realizar? \n'
    '1 para consulta por nome;\n'
    '2 para consulta por cpf;\n'
    '3 para mostrar funcionários por departamento;\n'
    '4 para adicionar novos funcionários;\n'
    '5 para remover funcionário por cpf;\n'
    '6 para alterar informaçoes de um funcionário;\n' \
    '0 para sair.'))
    
    match acao:

        case 1:
            consulta_por_nome(bancodados)
            continue

        case 2:
            consulta_por_cpf(bancodados)
            continue

        case 3:
            consulta_por_departamento(bancodados)
            continue

        case 4:
            adicionar_funcionário(bancodados)
            continue

        case 5:
            remover_por_cpf(bancodados)
            continue

        case 6:
            alteracao_por_cpf(bancodados)
            continue

        case _:
            break
