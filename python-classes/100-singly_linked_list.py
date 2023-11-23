#!/usr/bin/python3
""" A class about something u don't know"""


class Node:
    """A class representing a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node.

        Parameters:
        - data (int): The data to be stored in the node.
        - next_node (Node or None): The next node in the linked list.

        Raises:
        - TypeError: If data is not an integer or next_node is not a Node object.
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


class SinglyLinkedList:
    """A class representing a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list (increasing order).

        Parameters:
        - value (int): The value to be inserted into the linked list.
        """
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Return a string representation of the linked list.

        Returns:
        - str: The string representation of the linked list.
        """
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result[:-1]  # Remove the trailing newline for the last node
