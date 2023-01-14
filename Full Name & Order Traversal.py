# DATA STRUCTURE- ACTIVITY
print("PROGRAMMED BY:")
print("IREANNE N. OMEGA")
print("BSCOE 2-2\n")

# This section contains my full name
# and sorting it in order

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:

            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    print("My Full Name:",elements)

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    print("-------------------------------------------------------------------------------\n")
    fullname = ["I", "R", "E", "A", "N", "N", "E",
                "N",
                "O", "M", "E", "G", "A"]
    fullname_tree = build_tree(fullname)
    print("Full Name in Sorted Order:", fullname_tree.in_order_traversal())
    print("\n-------------------------------------------------------------------------------")