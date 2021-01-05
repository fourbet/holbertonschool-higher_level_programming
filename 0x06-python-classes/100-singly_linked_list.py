class Node:
    """ Class Node that defines a node of a singly linked list """

    def __init__(self, data, next_node=None):
        """ initialization of the class Node """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if not isinstance(next_node, Node) and 
            not isinstance(next_node, None):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data
        
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(next_node, Node) and
            not isinstance(next_node, None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """ Class SinglyLinkedList that defines a singly linked list """

    def __init__(self):
        """ initialization of an instance of SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        if self.__head == None:
            n1 = Node(value)
            self.__head = n1
        else:
            n2 = Node(value)
            (self.__head).next_node = n2
            self.__head

