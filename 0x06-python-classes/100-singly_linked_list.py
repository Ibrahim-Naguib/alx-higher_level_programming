#!/usr/bin/python3

"""define Classes for singly linked list."""


class Node:
    """Represent a node in a Singly linked list."""
    def __init__(self, data, next_node=None):

        """Initialize a Singly linked list

        Args:
            data (int): The data stored in the node.
            next_node (Node): Reference to the next node in the linked list.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Return the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node.

        Args:
            value (int): The new data for the node.

        Raises:
            TypeError: If the data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Return the next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node.

        Args:
            value (Node or None): The new next node.

        Raises:
            TypeError: If the next node is not a Node object or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a Singly linked list class."""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node with a sorted value.

        Args:
            value (int): The value to be inserted into the linked list.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """Return a string representation of the linked list."""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
