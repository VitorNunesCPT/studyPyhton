class Produto:
    def __init__(self, codigo, nome, preco, estoque):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def __str__(self):
        return f"Código: {self.codigo}\nNome: {self.nome}\nPreço: {self.preco}\nEstoque: {self.estoque}"


class CRUDProdutos:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, codigo, nome, preco, estoque):
        if isinstance(nome, str) and not nome.isdigit():
            produto = Produto(codigo, nome, preco, estoque)
            self.produtos.append(produto)
            print("Produto adicionado com sucesso!")
        else:
            print("Nome inválido. Certifique-se de que o nome seja uma string não numérica.")


    def buscar_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                print(produto)
                return
        print("Produto não encontrado.")

    def atualizar_produto(self, codigo, nome=None, preco=None, estoque=None):
        for produto in self.produtos:
            if produto.codigo == codigo:
                if nome and (not isinstance(nome, str) or nome.isdigit()):
                    print("Nome inválido. Certifique-se de que o nome seja uma string não numérica.")
                    return
                if preco and not isinstance(preco, float):
                    print("Preço inválido. Certifique-se de que o preço seja um número decimal.")
                    return
                if estoque and not isinstance(estoque, int):
                    print("Estoque inválido. Certifique-se de que o estoque seja um número inteiro.")
                    return
                
                if nome:
                    produto.nome = nome
                if preco:
                    produto.preco = preco
                if estoque:
                    produto.estoque = estoque
                print("Produto atualizado com sucesso!")
                return
        print("Produto não encontrado.")
        
    def excluir_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                self.produtos.remove(produto)
                print("Produto excluído com sucesso!")
                return
        print("Produto não encontrado.")

    def listar_produtos(self):
        if len(self.produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            for produto in self.produtos:
                print(produto)
                print("--------------------")


crud = CRUDProdutos()

while True:
    print("----- Gerenciador de produtos -----")
    print("1 - Adicionar produto")
    print("2 - Buscar produto")
    print("3 - Atualizar produto")
    print("4 - Excluir produto")
    print("5 - Listar produtos")
    print("0 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção inválida. Digite um número correspondente à opção desejada.")
        continue

    if opcao == 1:
        try:
            codigo = int(input("Digite o código do produto: "))
            nome = input("Digite o nome do produto: ")

            preco = float(input("Digite o preço do produto: "))
            estoque = int(input("Digite a quantidade em estoque do produto: "))
            crud.adicionar_produto(codigo, nome, preco, estoque)
        except ValueError:
            print("Valores inválidos. Certifique-se de que o código seja um número inteiro, o preço seja um número decimal e o estoque seja um número inteiro.")

    elif opcao == 2:
        try:
            codigo = int(input("Digite o código do produto: "))
            crud.buscar_produto(codigo)
        except ValueError:
            print("Código inválido. O código do produto deve ser um número inteiro.")

    elif opcao == 3:
        try:
            codigo = int(input("Digite o código do produto: "))
            nome = input("Digite o novo nome do produto (ou deixe em branco para não alterar): ")
            preco = input("Digite o novo preço do produto (ou deixe em branco para não alterar): ")
            estoque = input("Digite a nova quantidade em estoque do produto (ou deixe em branco para não alterar): ")

            if estoque:
                estoque = int(estoque)

            if preco:
                preco = float(preco)

            crud.atualizar_produto(codigo, nome, preco, estoque)
        except ValueError:
            print("Valores inválidos. Certifique-se de que o código seja um número inteiro, o preço seja um número decimal e o estoque seja um número inteiro.")

    elif opcao == 4:
        try:
            codigo = int(input("Digite o código do produto: "))
            crud.excluir_produto(codigo)
        except ValueError:
            print("Código inválido. O código do produto deve ser um número inteiro.")

    elif opcao == 5:
        crud.listar_produtos()

    elif opcao == 0:
        break

    else:
        print("Opção inválida. Tente novamente.")