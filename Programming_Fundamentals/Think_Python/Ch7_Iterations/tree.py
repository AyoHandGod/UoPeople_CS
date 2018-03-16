from anytree import Node, RenderTree

base = Node("Base")
right = Node("Branch right", parent=base)
right_split1 = Node("3 Pm Ticket", parent=right, value=200, probability=.6)
right_split2 = Node("Missed Train", parent=right, value=600, probability=.4)
left = Node("6 Pm Ticket", parent=base, value=400)
right.value = (right_split1.value * right_split1.probability) + (right_split2.value * right_split2.probability)

if right.value > left.value:
    print("Too High")
else:
    print("Just right")

print(right.value)


def brancher(tree):




class Tree(object):

    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = None

