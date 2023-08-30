#!/usr/bin/python3
"""Defines the classes for singly-linked list"""


class Node:
    """Represents node in the singly-linked list"""

    def __init__(self, data, next_node=None):
        """Initializes new Node

        Args:
            data (int): data for the new Node
            next_node (Node): next node for the new Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets or sets data of the Node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets or sets next_node of the Node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents singly-linked list"""

    def __init__(self):
        """Initalizes new SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts new Node to the SinglyLinkedList

        The node is inserted into the list at correct
        ordered numerical position

        Args:
            value (Node): New Node to be inserted
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Defines the print() representation of SinglyLinkedList"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
