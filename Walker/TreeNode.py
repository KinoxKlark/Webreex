class TreeNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []
    def attach(self, child):
        p = self.parent
        while p is not None:
            p = p.parent
            if p == child:
                raise Exception('You should not attach a parent to his child')
        if child.parent != None:
            child.parent.children.remove(child)
        child.parent = self
        self.children.append(child)
        return self

    def detach(self, child):
        self.children.remove(child)
        child.parent = None
        return child
