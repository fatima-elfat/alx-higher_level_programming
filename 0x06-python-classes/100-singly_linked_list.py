#!/usr/bin/python3
"""
Class Node
Class SinglyLinkedList
"""


class Node:
    """
    Definition of class Node.

    Args:
       __data (int): value in node.
       __next_node : next node, Null if head.
    """
    __data = None
    __next_node = None

    def __init__(self, data, next_node=None):
        """
        Initializes the node.

        Attributes:
            data (int): value in node.
            next_node : next node, Null if head.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """"
        Getter function.

        Return: value in node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter function.

        Args:
            value: the value to set in data (value node).
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """"
        Getter function.

        Return: next node type class node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter

        Args:
            value: the value of the next node.
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    Definition of class SinglyLinkedList.

    Args:
        __head: head of the singly linked lis type Node.
    """
    __head = None

    def __init__(self):
        """
        Initializes the SinglyLinkedList.

        Attributes:
            head: the head of SinglyLinkedList.
        """
        self.__head = None

    def __str__(self):
        """
        Creates the value be printable.

        Return: r the string value.
        """
        r = ""
        l_h = self.__head
        while l_h is not None:
            r += str(l_h.data)
            l_h = l_h.next_node
            if l_h is not None:
                r += "\n"
        return r

    def sorted_insert(self, value):
        """
        Inserts new nodes into the correct sorted position
        in the list (increasing order)

        Args:
        value: data value in the node.

        Raises:
            TypeError: If `value` type is not `int`.
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        nod = Node(value)
        if self.__head is None:
            self.__head = nod
            return
        if nod.data < self.__head.data:
            nod.next_node = self.__head
            self.__head = nod
            return
        nod2 = self.__head
        while (nod2.next_node.data < nod.data and nod2.next_node is not None):
            nod2 = nod2.next_node
        nod.next_node = nod2.next_node
        nod2.next_node = nod
        return
