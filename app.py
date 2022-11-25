class Tree:
    def __init__(self, val=None, descricao=None, fornecedor=None, preco=None, amount=None):
        self.left = None
        self.right = None
        self.val = val
        self.des = descricao
        self.frd = fornecedor
        self.prc = preco
        self.qnt = amount

    def insert(self, val, description, provider, price, amount):
        if not self.val:
            self.val = val
            self.des = description
            self.frd = provider
            self.prc = price
            self.qnt = amount
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val, description, provider, price, amount)
                return
            self.left = Tree(val, description, provider, price, amount)
            return

        if self.right:
            self.right.insert(val, description, provider, price, amount)
            return
        self.right = Tree(val, description, provider, price, amount)

    def existe(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.existe(val)

        if self.right == None:
            return False
        return self.right.existe(val)

    def deletar(self, val):
        if self == None:
            return self

        if val < self.val:
            if self.left:
                self.left = self.left.deletar(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.deletar(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.deletar(min_larger_node.val)
        return self
   
    def deletar_aux(self, val):
        x = root.existe(val)
        if x is True:
            if self.val == val and self.right is None and self.left is None:
                self.left, self.right, self.val, self.des, self.frd, self.prc, self.qnt = None, None, None, None, None, None, None
                return
            if self == None:
                return self
            if val < self.val:
                if self.left:
                    self.left = self.left.deletar(val)
                return self
            if val > self.val:
                if self.right:
                    self.right = self.right.deletar(val)
                return self
            if self.right == None:
                return self.left
            if self.left == None:
                return self.right
            min_larger_node = self.right
            while min_larger_node.left:
                min_larger_node = min_larger_node.left
            self.val = min_larger_node.val
            self.right = self.right.deletar(min_larger_node.val)
            return self  

    def change_price(self, val, nprc):
        if root.existe(val) is True:
            if self.val == val:
                self.prc = nprc
            if val < self.val:
                if self.left:
                    self.left.change_price(val, nprc)
                return
            if val > self.val:
                if self.right:
                    self.right.change_price(val, nprc)
                return
            return
        return

    def change_amount(self, val, nqnt):
        if root.existe(val) is True:
            if self.val == val:
                self.qnt = nqnt
            if val < self.val:
                if self.left:
                    self.left.change_amount(val, nqnt)
                return
            if val > self.val:
                if self.right:
                    self.right.change_amount(val, nqnt)
                return
            return
        return

    def show_all(self, val):
        if val == self.val:
            print('PRODUTO: {}, CÓDIGO: {}, FORNECEDOR: {}, PREÇO: R${}, QUANTIDADE EM ESTOQUE: {}'
                  .format(self.des, self.val, self.frd, self.prc, self.qnt))
            return

        if val < self.val:
            if self.left:
                self.left.show_all(val)
                return
            print(self.val, self.des, self.frd, self.prc, self.qnt)
            return

        if self.right:
            self.right.show_all(val)
            return
        print(self.val, self.des)

        if self.right == None:
            return False
        return self.right.existe(val)

    def inorde2(self, vals):
        if self.left is not None:
            self.left.inorde2(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorde2(vals)
        return vals


root = Tree()

class Cadastro:
    def add_product(self):
        print('\nDIGITE O CÓDIGO DO PRODUTO\n')
        code = input()
        print('\nDIGITE A DESCRIÇÃO DO PRODUTO\n')
        description = input()
        print('\nDIGITE O FORNECEDOR DO PRODUTO\n')
        provider = input()
        print('\nDIGITE O PREÇO DO PRODUTO\n')
        price = float(input())
        print('\nDIGITE A QUANTIDADE DISPONÍVEL DO PRODUTO\n')
        amount = int(input())
        root.insert(code, description, provider, price, amount)

        m.app()

    def excluir(self):
   
        print('\nDIGITE O CÓDIGO DO PRODUTO QUE DESEJA EXCLUIR')
        x = int(input())

        root.deletar_aux(x)

        m.app()

    def search(self):
 
        print('\nDIGITE O CÓDIGO DO PRODUTO DESEJADO')
        x =input()

        if root.existe(x) is True:
            print('\nPRODUTO DISPONÍVEL EM ESTOQUE')
        else:
            print('\nPRODUTO NÃO ENCONTRADO')

        m.app()

    def view(self):
        x = root.inorde2([])
        for y in x:
            root.show_all(y)

        m.app()

    def produto_espec(self):
        print('\nVISUALIZAR PRODUTO')

        print('\nDIGITE O CÓDIGO DO PRODUTO')
        x = input()
        root.show_all(x)

        m.app()

    def change(self):

        print('   (0) BACK TO MAIN MENU\n'
              '   (1) MUDAR PREÇO\n'
              '   (2) MUDAR QUANTIDADE DISPONÍVEL\n'
              )
        x = input()
        if x == '1':
            print("\nESTOQUE\n")
            x = root.inorde2([])
            for y in x:
                root.show_all(y)
            print('\nDIGITE O CODIGO DO ITEM A SER ALTERADO\n')
            product_code = input()

            print('\nDIGITE O NOVO PREÇO\n')
            newprice = float(input())
            root.change_price(product_code,newprice)

            print('\nPREÇO ALTERADO COM SUCESSO\n')
            m.app()

        elif x == '2':
            print("\nESTOQUE\n")
            x = root.inorde2([])
            for y in x:
                root.show_all(y)
            print('\nDIGITE O CODIGO DO ITEM A SER ALTERADO\n')
            product_code = input()

            print('\nDIGITE A NOVA QUANTIDADE DO ESTOQUE\n')
            new_amount = int(input())
            root.change_amount(product_code,new_amount)

            print('\nQUANTIDADE EM ESTOQUE ALTERADA COM SUCESSO\n')

            m.app()
        else:
            m.app()


c = Cadastro() 

class Main:
    def app(self):
        print(' \n   (0)  SAIR\n'
              '   (1) CADASTRAR PRODUTO\n'
              '   (2) VISUALIZAR ESTOQUE\n'
              '   (3) PROCURAR PRODUTO\n'
              '   (4) ALTERAR PRODUTOS\n'
              '   (5) VER INFORMAÇÕES DO PRODUTO\n'
              '   (6) EXCLUIR PRODUTO\n'
              )
        x = input()
        if x == '0':
            print("OBRIGADO POR USAR NOSSOS SEVIÇOS,VOLTE SEMPRE")
            quit()
        elif x == '1':
            c.add_product()
        elif x == '2':
             c.view()
        elif x == '3':
            c.search()
        elif x == '4':
            c.change()
        elif x == '5':
            c.produto_espec()
        elif x == '6':
            c.excluir()
        else:
          print("DIGITE UM VALOR VÁLIDO")
          m.app()

m = Main()

m.app()