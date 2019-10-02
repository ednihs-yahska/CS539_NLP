class Node:
    def __init__(self, symbol):
        self.symbol = symbol
        self.label=""
        self.children = []

def search(symbol, list):
    for node in list:
        if symbol == node.symbol:
            return node
    return None

def debug_print(level):
    for node in level:
        print("Level "+node.symbol)
    print()

class PrefixTree:
    def __init__(self):
        self.root = Node('*')
        self.root.label = '*'

    def insert(self, string):
        currentNode = self.root
        label=""
        for symbol in string:
            if not symbol.isspace():
                label = label + symbol
                level = currentNode.children
                target = search(symbol, level)
                #debug_print(level)
                if target is None:
                    n = Node(symbol)
                    currentNode = n
                    n.label=label
                    level.append(n)
                else:
                    currentNode = target
        label=""

    def fsa(self):
        fst="F\n"
        return self.print_fsa(self.root, fst)
                
    def print_fsa(self, node, fst):
        fst = fst + '( '+node.label
        level = node.children
        if len(level) == 0:
            return node.label+'))'
        else:
            while len(level)>0:
                debug_print(level)
                new_symbol = level.pop()
                print("Popped "+new_symbol.symbol)
                fst = fst + ' ('+new_symbol.label+' '+new_symbol.symbol+'))\n'
                print(fst)
                self.print_fsa(new_symbol, fst)
        return fst

tree = PrefixTree()
for line in open('vocab.small'):
    print("Inserting line "+str(line))
    tree.insert(line)
    print("Line inserted")
print("--Printing--")
tree.fsa()


