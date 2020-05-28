class Node:

    def __init__(self, element):
        self.element = element
        self.children = []
        self.index = []


    def has_children(self):
        if len(self.children) > 0:
            return True
        else:
            return False

class Trie:
    def __init__(self, text):
        self.root = Node('Root placeholder')
        self.sort(text)

    def sort(self, text):
        skip = [' ', '.', ',', '!', ':', ';']
        index = 0
        while index < len(text):
            print('Checking ' + text[index])
            if text[index] in skip:
                index += 1
            else:
                index = self.insert(text, index, skip)

    def insert(self, text, index, skip):
        #Her er det sikkert at orden begyner med en bogstav
        node = self.root
        innerindex = index
        while innerindex < len(text) and text[innerindex] not in skip:
            if node.has_children():
                i = 0
                while i < len(node.children): #TODO make pretty
                    print('text: ' + text[innerindex])
                    print('childelement: ' + node.children[i].element)
                    if text[innerindex] == node.children[i].element:
                        node = node.children[i]
                        i = 100000
                    elif text[innerindex] < node.children[i].element:
                        newnode = Node(text[innerindex])
                        node.children.append(i, newnode)
                        node = newnode
                        print('Created ' + newnode.element)
                        break
                    i += 1
            else:
                newnode = Node(text[innerindex])
                node.children.append(newnode)
                node = newnode
                print('Created ' + newnode.element)
            innerindex += 1


        node.index.append(index)
        return innerindex

    def printme(self):
        for r_child in self.root.children:
           self.print_triversal(r_child)

    def print_triversal(self, node):
        print(node.element)
        if node.has_children():
            for child in node.children:
                return self.print_triversal(child)
        else:
            print('Word over')
            return



if 'e' == 'e':
    print('same')
else:
    print('different')

text = 'Made er bare mega sej'
trie = Trie(text)
trie.printme()