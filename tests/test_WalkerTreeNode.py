import unittest
from Walker.TreeNode import TreeNode

class TestWalkerTreeNode(unittest.TestCase):

    def setUp(self):
        self.root = TreeNode("root")
        self.c1 = TreeNode("child1")
        self.c2 = TreeNode("child2")
        self.c3 = TreeNode("child3")

    def test_creation(self):
        """
            Test the creation of a tree
        """
        self.assertEqual(self.root.value, "root")
        self.assertEqual(self.root.children, [])

    def test_attach(self):
        """
            Test the attach functionality
        """

        # Attach multiple node to root
        r2 = self.root.attach(self.c1).attach(self.c2)
        self.assertEqual(self.root.children, [self.c1,self.c2])
        self.assertEqual(self.c1.parent, self.root)
        self.assertEqual(self.c2.parent, self.root)
        self.assertEqual(r2, self.root)

        # Attach a node to a subnode
        self.c1.attach(self.c3)
        self.assertEqual(self.c1.children, [self.c3])
        self.assertEqual(self.c2.children, [])
        self.assertEqual(self.c3.parent, self.c1)

        # Attach a node who already have a parent
        self.c2.attach(self.c3)
        self.assertEqual(self.c1.children, [])
        self.assertEqual(self.c2.children, [self.c3])
        self.assertEqual(self.c3.parent, self.c2)

    def test_detach(self):
        """
            Test the detach functionality
        """
        self.root.attach(self.c1).attach(self.c2)
        self.c1.attach(self.c3)

        self.assertEqual(self.c1.children, [self.c3])
        self.assertEqual(self.c3.parent, self.c1)

        c4 = self.c3.detach()
        self.assertEqual(self.c1.children, [])
        self.assertEqual(self.c3.parent, None)
        self.assertEqual(self.c3, c4)

    def test_parent_check(self):
        """
        Check if a node is parent of another
        :return:
        """
        self.root.attach(self.c1).attach(self.c2)
        self.c2.attach(self.c3)

        self.assertFalse(self.root.has_parent(self.c1))
        self.assertFalse(self.c3.has_parent(self.c1))
        self.assertFalse(self.c2.has_parent(self.c1))

        self.assertTrue(self.c1.has_parent(self.root))
        self.assertTrue(self.c3.has_parent(self.c2))
        self.assertTrue(self.c3.has_parent(self.root))

    def test_loop(self):
        """
            Test that an exception is raise if we try to attach a parent to a children
        """
        self.c2.attach(self.c3)
        self.c1.attach(self.c2)
        self.root.attach(self.c1)

        # Test to attach a parent to a children
        with self.assertRaises(Exception):
            self.c3.attach(self.c1)

        self.assertEqual(self.c1.parent, self.root)
        self.assertEqual(self.c1.children, [self.c2])
        self.assertEqual(self.root.children, [self.c1])

        self.assertEqual(self.c3.parent, self.c2)
        self.assertEqual(self.c3.children, [])
        self.assertEqual(self.c2.children, [self.c3])

        # Test to attach a node to itself
        with self.assertRaises(Exception):
            self.c2.attach(self.c2)

        self.assertEqual(self.c2.parent, self.c1)
        self.assertEqual(self.c2.children, [self.c3])
        self.assertEqual(self.c1.children, [self.c2])
