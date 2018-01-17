class TreeNode:
    """
    Simple tree structure. A node hold a value and can have multiple children
    A node can only appear once in the tree
    A node can not have one of his parents in his children
    """

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

    def attach(self, child):
        """
        Check if the child can be attach to the node and attach it
        :param child  A tree node to attach to the called node
        :return self
        """
        if child is self:
            raise TreeNodeException('You should not attach a child to himself')
        if self.has_parent(child):
            raise TreeNodeException('You should not attach a parent to his child')
        if child.parent is not None:
            child.parent.children.remove(child)
        child.parent = self
        self.children.append(child)
        return self

    def detach(self):
        """
        Detach the current node from his parent
        :return self
        """
        self.parent.children.remove(self)
        self.parent = None
        return self

    def has_parent(self, node):
        """
        Check if the given node is a parent of himself
        :param  node The node to check if parent
        :return True if the given node is a parent
        """
        p = self.parent
        while p is not None:
            if p == node:
                return True
            p = p.parent
        return False


class TreeNodeException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
