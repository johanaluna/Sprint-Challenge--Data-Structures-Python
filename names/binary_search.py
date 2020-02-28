
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value is found, return false to indicate no node inserted
        # if self.value == value:
        #     pass
        # value smaller than node, look left
        if value < self.value:
            # if node exists, continue recursively checking until something is found or inserted
            if self.left:
                return self.left.insert(value)
            # if no node exists, create new one and return true
            else:
                self.left = BinarySearchTree(value)
                return(value,'Added')
        if value >= self.value:
            # if node exists, continue recursively checking until something is found or inserted
            if self.right:
                return self.right.insert(value)
            # if no node exists, create new one and return true
            else:
                self.right = BinarySearchTree(value)
                return(value,'Added')
    
    def contains(self, target):
        if target== self.value:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False