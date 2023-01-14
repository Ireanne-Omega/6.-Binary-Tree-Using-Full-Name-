# DATA STRUCTURE- ACTIVITY
print("PROGRAMMED BY:")
print("IREANNE N. OMEGA")
print("BSCOE 2-2\n")

# ======================== ==============================
# This section contains all the summarize codes
# =======================================================

# define class statement
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

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            minimum_val = self.right.minimum()
            self.data = minimum_val
            self.right = self.right.delete(minimum_val)

        return self

    def minimum(self):
        if self.left is None:
            return self.data
        return self.left.minimum()

    def maximum(self):
        if self.right is None:
            return self.data
        return self.right.maximum()


def build_tree(elements):
    print("My Full name:", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

  # ======================== if __name__ statement ==============================
if __name__ == '__main__':
    print("-------------------------------------------------------------------------------\n")
    fullname = ["I", "R", "E", "A", "N", "N", "E",
                "N",
                "O", "M", "E", "G", "A"]
    fullname_tree = build_tree(fullname)

    # ======================== print statements ==============================
    print("\nFull Name in Sorted Order:", fullname_tree.in_order_traversal())
    print("Full Name in Pre-Order:", fullname_tree.pre_order_traversal())
    print("Full Name in Post-Order:", fullname_tree.post_order_traversal())
    print("\nMinimum Value:", fullname_tree.minimum())
    print("Maximum Value:", fullname_tree.maximum())
    print("\nIs T found inside the list?", fullname_tree.search("T"))
    print("Is E found inside the list?", fullname_tree.search("E"))
    fullname_tree.delete("I")
    print("\nI was removed inside the list:", fullname_tree.in_order_traversal())
    fullname_tree.delete("R")
    print("R was removed inside the list:", fullname_tree.in_order_traversal())
    print("\n-------------------------------------------------------------------------------")
