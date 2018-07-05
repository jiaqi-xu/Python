# -*- encoding: utf-8 -*-
"""
    File name: check_same_tree.py
    Author: Jiaqi Xu <http:jqx.world>
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def is_the_same_tree(self, p, q):
        if p is None and q is None:
            return True

        if p is None or q is None or p.value != q.value:
            return False

        return (
            self.is_the_same_tree(p.left, q.left)
            and self.is_the_same_tree(p.right, q.right)
        )
