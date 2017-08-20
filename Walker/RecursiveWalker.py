from Walker import Walker

class RecursiveWalker(Walker):

    def walk(self):
        """Walk recursively in all possible pages"""
        i = 0
        while i < len(self.urls) and self.depth <= self.config['max_depth']:
            if self.walkTo(self.urls[i]):
                i += 1