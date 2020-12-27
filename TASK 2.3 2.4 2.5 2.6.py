class Node:
    def __init__(self, content, left_pointer, right_pointer):
        self.content = content
        self.left_pointer = left_pointer
        self.right_pointer = right_pointer

    def print_tree_based_on_node(self, array):
        if self.left_pointer is not None:
            array[self.left_pointer].print_tree_based_on_node(array)
        print(self.content, end=' ')
        if self.right_pointer is not None:
            array[self.right_pointer].print_tree_based_on_node(array)

class Tree:
    def __init__(self):
        self.content = [Node('maroon', 1, 2), Node('black', 3, 5), Node('silver', 7, 8), Node('amber', None, None),
                        Node('indigo', 5, 6), Node('grey', None, None), Node('lime green', None, None),
                        Node('red', None, None), Node('violet', None, None)]
        self.root = 0

    def adding_data_item(self, data_item):
        self.content.append(Node(data_item, None, None))
        current_pointer = self.root
        while current_pointer is not None:
            previous_pointer = current_pointer
            if self.content[current_pointer].content > data_item:
                turned_left = True
                current_pointer = self.content[current_pointer].left_pointer
            else:
                turned_left = False
                current_pointer = self.content[current_pointer].right_pointer
        if turned_left is True:
            self.content[previous_pointer].left_pointer = len(self.content) - 1
        else:
            self.content[previous_pointer].right_pointer = len(self.content) - 1

    def find_specific_colour(self, colour):
        current_pointer = self.root
        while self.content[current_pointer].content != colour:
            if self.content[current_pointer].content > colour:
                current_pointer = self.content[current_pointer].left_pointer
            else:
                current_pointer = self.content[current_pointer].right_pointer
            if current_pointer is None:
                break
        return current_pointer

    def print_tree(self):
        self.content[1].print_tree_based_on_node(self.content)
        print('')

