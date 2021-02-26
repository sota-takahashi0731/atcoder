class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        #Nodeクラスのインスタンスを文字列表現
        left = f'[{self.left.value}]' if self.left else '[]'
        right = f'[{self.right.value}]' if self.right else '[]'
        return f'{left} <- {self.value} -> {right}'

class BinarySearchTree:

    def __init__(self):
        self.nodes = []

    def add_node(self, value):
        node = Node(value)
        if self.nodes:
            parent, direction = self.find_parent(value)
            if direction == 'left':
                parent.left = node
            else:
                parent.right = node
        #この木のノードとして格納
        self.nodes.append(node)

    def find_parent(self, value):
        node = self.nodes[0]
        #nodeがNoneになるまで（葉にたどり着くまで）ループを回す
        while node:
            p = node
            if p.value == value:
                raise ValueError('すでにある値と同じ値を格納することはできません.')
            if p.value > value:
                direction = 'left'
                node = p.left
            else:
                direction = 'right'
                node = p.right
        return p, direction

import random

tree = BinarySearchTree()
for i in range(10):
    v = random.randint(0,99)
    tree.add_node(v)

for node in tree.nodes:
    print(node)
