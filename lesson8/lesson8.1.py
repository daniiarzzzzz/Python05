class Human:

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent


node0 = Human("Adam", None)
node1 = Human("Joobasar", node0)
node2 = Human("Tenesh", node1)
node3 = Human("Kary", node2)
node4 = Human("Tokol", node3)
node5 = Human("Baytugol", node4)
node6 = Human("Apytai", node5)
node7 = Human("Ajybek", node6)
node8 = Human("Kalygul", node7)
node9 = Human("Abakir", node8)
node10 = Human("Maken", node9)
node11 = Human("Jambul", node10)

node12 = Human("Azisbek", node11)

n = node12

while n.name != "Adam":
    print(n.name)
    n = n.parent
