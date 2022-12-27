# Singly Linked Lists

### Challenge

- Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
- Create a Linked List class with a head property.
  - Upon instantiation, an empty Linked List should be created.
    - The class should contain the following methods
      - insert
        - Arguments: value
        - Returns: nothing
        - Adds a new node with that value to the head of the list with an O(1) Time performance.
      - includes
        - Arguments: value
        - Returns: Boolean
        - Indicates whether that value exists as a Node’s value somewhere within the list.
      - to string
        - Arguments: none
        - Returns: a string representing all the values in the Linked List, formatted as: "{ a } -> { b } -> { c } -> NULL"

### Approach & Efficiency

- Creating Node and using Node class, adding nodes to the LinkedList class.

### API

- insert => Adds a new node with that value to the head of the list with an O(1) Time performance.
- includes => Indicates whether that value exists as a Node’s value somewhere within the list.
- to string => Returns a string representing all the values in the Linked List, formatted as: "{ a } -> { b } -> { c } -> NULL"
