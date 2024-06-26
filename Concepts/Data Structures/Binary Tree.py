class BinaryTreeNode():
    def __init__(self, value=None, right=None, left=None):
        self.data = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.left} <- {self.data} -> {self.right}"

    def Insert(self, value):
        if self.data:

            if value > self.data:
                if self.right == None:
                    self.right = BinaryTreeNode(value)
                else:
                    self.right.Insert(value)

            elif value < self.data:
                if self.left == None:
                    self.left = BinaryTreeNode(value)
                else:
                    self.left.Insert(value)

        else:
            self.data = value

    def Search(self, value):
        if self.data:

            if self.data == value:
                print("Found")

            elif value > self.data:
                if self.right != None:
                    self.right.Search(value)
                else:
                    print("Not Found")

            elif value < self.data:
                if self.left != None:
                    self.left.Search(value)
                else:
                    print("Not Found")

        else:
            print("Tree Is Empty")

    # Left, Data (Print) , Right
    def InOrderTraversal(self):
        Result = []

        if self.left:
            self.left.InOrderTraversal()

        Result.append(self.data)

        if self.right():
            self.right.InOrderTraversal()

        return Result

    # Left (Print), Data, Right
    def PreOrderTraversal(self):
        Result = []

        Result.append(self.data)

        if self.left:
            self.left.PreOrderTraversal()

        if self.right:
            self.right.PreOrderTraversal()

        return Result

    # Left, Data, Right (Print)
    def PostOrderTraversal(self):
        Result = []

        if self.right:
            self.right.PostOrderTraversal()

        Result.append(self.data)

        if self.left:
            self.left.PostOrderTraversal()

        return Result