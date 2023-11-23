#!/usr/bin/python3
"""pthon advance """


class Node:
    """A class representing a node of a
    singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node.

        Parameters:
        - data (int): The data to be stored in the node.
        - next_node (Node or None): The next node in 
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node in the linked list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the linked list."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
