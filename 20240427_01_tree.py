class TreeNode:
    def __init__(self, data, children=None):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = "-   " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def add_child(self, tree_node):
        self.children.append(tree_node)


tree = TreeNode("Drinks", [])
soft = TreeNode("Soft", [])
hard = TreeNode("Hard", [])
tree.add_child(soft)
tree.add_child(hard)
tea = TreeNode("Tea", [])
coffee = TreeNode("Coffee", [])
soft.add_child(tea)
soft.add_child(coffee)
wine = TreeNode("Wine", [])
beer = TreeNode("Beer", [])
hard.add_child(wine)
hard.add_child(beer)
green = TreeNode("Green", [])
black = TreeNode("Black", [])
lemon = TreeNode("Lemon", [])
milk = TreeNode("Milk", [])
tea.add_child(green)
tea.add_child(black)
tea.add_child(lemon)
tea.add_child(milk)
americano = TreeNode("Americano", [])
cappuccino = TreeNode("Cappuccino", [])
espresso = TreeNode("Espresso", [])
mocha = TreeNode("Mocha", [])
coffee.add_child(americano)
coffee.add_child(cappuccino)
coffee.add_child(espresso)
coffee.add_child(mocha)
print(tree)
