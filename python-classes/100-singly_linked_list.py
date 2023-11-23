#!/usr/bin/python3
""" python classes"""


class Node:
    """
    A class representing a node of a singly linked list.

    Attributes:
    - data (int): The data stored in the node.
    - next_node (Node or None): The reference to the next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node with the given data and next_node.

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
        """
        Retrieves the data stored in the node.

        Returns:
        - int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node.

        Parameters:
        - value (int): The data to be set.

        Raises:
        - TypeError: If the provided value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the linked list.

        Returns:
        - Node or None: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list.

        Parameters:
        - value (Node or None): The next node in the linked list.

        Raises:
        - TypeError: If the provided value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class representing a singly linked list.

    Attributes:
    - head: The head node of the linked list.
    """

    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

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
        Returns a string representation of the linked list.

        Returns:
        - str: The string representation of the linked list.
        """
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result[:-1]  # Remove the trailing newline for the last node
