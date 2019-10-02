class Node:
    def __init__(self, symbol):
        self.symbol = symbol
        self.children = []

def search(symbol, list):
    for node in list:
        if symbol == node.symbol:
            return node
    return None

class PrefixTree:
    def __init__(self):
        self.roots=[]

    def insert(self, symbol):
        level = self.roots
        print("Length of level "+ str(len(level)))
        target = search(symbol, level)
        while target:   
            level = target.children
            target = search(symbol, level)
        level.append(Node(symbol))
    
    def levelPrinter(self, level):
        for symbol in level:
            print(symbol.symbol, end=" ")
        print("--")

    def print(self, level):
        while len(level)>0: 
            self.levelPrinter(level)  
            for node in level:
                level = node.children
                self.print(level)
   
        
tree = PrefixTree()
for line in open('vocab.small'):
    for symbol in line:
        if symbol != " ":
            print("Inserting symbol "+str(symbol))
            tree.insert(symbol)
            print("Symbol inserted")
print("--Printing--")
tree.print(tree.roots)
