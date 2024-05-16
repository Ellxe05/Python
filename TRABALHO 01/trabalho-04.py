#QUESTAO 04
print('Bem vindo a Livraria da Gabrielle Silva')
print('-' * 50)
print('                MENU PRINCIPAL')
print('-' * 50)

print('Escolha a opção desejada:')
print('1 - Cadastrar Livro')
print('2 - Consultar Livro(s)')
print('3 - Remover Livro')
print('4 - Sair')

lista_livro = []
id_global = 0

def cadastrar_livro(id):
    nome = input('Por favor entre com o nome do livro: ')
    autor = input('Por favor entre com o autor do livro: ')
    editora = input('Por favor entre com a editora do livro: ')
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livro.append(livro)

def consultar_livro():
    opcao = input('1 - Consultar Todos | 2 - Consultar por Id | 3 - Consultar por Autor | 4 - Retornar ao menu: ')
    if (opcao == '1'):
        for livro in lista_livro:
            print(livro)
    elif (opcao == '2'):
        consultando_id = input('Digite o id do livro: ')
        for livro in lista_livro:
            if (livro['id'] == consultando_id):
                print(livro)
                break
    elif (opcao == '3'):
        consultando_autor = input('Digite o autor do(s) livro(s): ')
        for livro in lista_livro:
            if (livro['autor'] == consultando_autor):
                print(livro)
    elif (opcao == '4'):
        return
    else:
        print('Opção inválida')

def remover_livro():
    remocao = input('Digite o id do livro a ser removido: ')
    for livro in lista_livro:
        if (livro['id'] == remocao):
            lista_livro.remove(livro)
            print('Livro removido com sucesso!')
            return
        else:
            print('Id inválido')

while True:
    opcao_escolhida = input('>>')
    if (opcao_escolhida == '1'):
        cadastrar_livro(id_global)
    elif (opcao_escolhida == '2'):
        consultar_livro()
    elif (opcao_escolhida == '3'):
        remover_livro()
    elif (opcao_escolhida == '4'):
        print('Encerrando...')
        break
    else:
        print('Opção inválida')