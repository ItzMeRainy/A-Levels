class BinaryTreeNode():
    def __init__(self, value=None, right=None, left=None):
        self.data = value
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"{self.left} <- {self.value} -> {self.right}"

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
                    self.right.Insert(value)
            
        else: 
            self.data = value

    def Search(self, value):
        pass