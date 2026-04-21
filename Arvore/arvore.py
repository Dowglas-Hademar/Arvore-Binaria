class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class Arvore:
    def __init__(self):
        self.root = None

    def add(self, value)-> bool:
        no = Node(value)
        if self.root is None:
            self.root = no
            return True

        perc = self.root
        while True:
            if value < perc.value:
                if perc.left is None:
                    perc.left = no
                    return True
                else: perc = perc.left
            elif value >= perc.value:
                if perc.right is None:
                    perc.right = no
                    return True
                else:
                    perc = perc.right

    def get(self, value):
        perc = self.root
        while perc:
            if value == perc.value:
                return perc.value
            elif value < perc.value:
                perc = perc.left
            elif value > perc.value:
                perc = perc.right

        return None


    def remove(self, value) :
        if self.root is None:
            return None

        perc = self.root
        perc2 = None

        while perc:
            if value == perc.value:
                break
            elif value < perc.value:
                perc2 = perc
                perc = perc.left
            elif value > perc.value:
                perc2 = perc
                perc = perc.right

        if perc is None:
            return None

        if perc.left is None and perc.right is None: #! se não tiver filhos
            if perc == self.root:
                self.root = None
            elif perc2.left == perc:
                perc2.left = None
            elif perc2.right == perc:
                perc2.right = None
            return True

        elif perc.left is None or perc.right is None: #! se tiver ao menos um filho
            if perc == self.root:
                if perc.left is not None:
                    self.root = perc.left
                else:
                    self.root = perc.right

            elif perc2.left == perc:
                if perc.left is not None:
                    perc2.left = perc.left
                else:
                    perc2.left = perc.right

            elif perc2.right == perc:
                if perc.left is not None:
                    perc2.right = perc.left
                else:
                    perc2.right = perc.right
            return True

        elif perc.left is not None and perc.right is not None: #! se tiver 2 filhos
            suc2 = perc #ANDA ATRAS DE SUC
            suc = perc.right #SUCESSOR DE PERC

            while suc.left:
                suc2 = suc
                suc = suc.left

            perc.value = suc.value

            if suc2.left == suc:
                suc2.left = suc.right
            elif suc2.right == suc:
                suc2.right = suc.right
            return True


    def print_ordem(self):
        def em_ordem(no):
            if no:
                em_ordem(no.left)
                print(no.value, end= " ")
                em_ordem(no.right)
        em_ordem(self.root)
        print()

        #https://pythonhelp.wordpress.com/2015/01/19/arvore-binaria-de-busca-em-python/
        # Verificar somente a parte de ordem, pre e pos odem

    def print_pre_ordem(self):
        def pre_ordem(no):
            if no:
                print(no.value, end= " ")
                pre_ordem(no.left)
                pre_ordem(no.right)
        pre_ordem(self.root)
        print()

    def print_pos_ordem(self):
        def pos_ordem(no):
            if no:
                pos_ordem(no.left)
                pos_ordem(no.right)
                print(no.value, end= " ")
        pos_ordem(self.root)
        print()

    def get_nivel_no(self, value):
        level = 0
        perc = self.root
        while perc:
            if value == perc.value:
                return level
            elif value < perc.value:
                perc = perc.left
                level += 1
            elif value >= perc.value:
                perc = perc.right
                level +=1
        return None

        #retornar o nivel do no

#TESTES
tree = Arvore()
ints = [10, 8, 6, 7, 13, 11, 14, 12, 5]

for num in ints:
    tree.add(num)

tree.print_ordem()




