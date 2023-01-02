# Stacks and Queues

A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner.

A queue is a collection of objects that supports fast first-in, first-out (FIFO) semantics for inserts and deletes.

## Challenge

Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

Node
Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.

Stack
Create a Stack class that has a top property. It creates an empty Stack when instantiated. The class should contain the following methods: push, pop, peek, and is_empty.

Queue
Create a Queue class that has a front property. It creates an empty Queue when instantiated. The class should contain the following methods: push, pop, peek, and is_empty.

## Approach & Efficiency

***Stack***
Create a Stack class that has a top property. It creates an empty Stack when instantiated.
This object should be aware of a default empty value assigned to top when the stack is created.

The class should contain the following methods:

- push
Arguments: value
adds a new node with that value to the top of the stack with an O(1) Time performance.

- pop
Arguments: none
Returns: the value from node from the top of the stack
Removes the node from the top of the stack
Should raise exception when called on empty stack

- peek
Arguments: none
Returns: Value of the node located at the top of the stack
Should raise exception when called on empty stack

- is_empty
Arguments: none
Returns: Boolean indicating whether or not the stack is empty.

***Queue***
Create a Queue class that has a front property. It creates an empty Queue when instantiated.
This object should be aware of a default empty value assigned to front when the queue is created.

The class should contain the following methods:

- enqueue
Arguments: value
adds a new node with that value to the back of the queue with an O(1) Time performance.

- dequeue
Arguments: none
Returns: the value from node from the front of the queue
Removes the node from the front of the queue
Should raise exception when called on empty queue

- peek
Arguments: none
Returns: Value of the node located at the front of the queue
Should raise exception when called on empty stack

- is_empty
Arguments: none
Returns: Boolean indicating whether or not the queue is empty

## API

Same as the section Approach and Efficiency

***Stack***
Create a Stack class that has a top property. It creates an empty Stack when instantiated.
This object should be aware of a default empty value assigned to top when the stack is created.

The class should contain the following methods:

- push
Arguments: value
adds a new node with that value to the top of the stack with an O(1) Time performance.

- pop
Arguments: none
Returns: the value from node from the top of the stack
Removes the node from the top of the stack
Should raise exception when called on empty stack

- peek
Arguments: none
Returns: Value of the node located at the top of the stack
Should raise exception when called on empty stack

- is_empty
Arguments: none
Returns: Boolean indicating whether or not the stack is empty.

***Queue***
Create a Queue class that has a front property. It creates an empty Queue when instantiated.
This object should be aware of a default empty value assigned to front when the queue is created.

The class should contain the following methods:

- enqueue
Arguments: value
adds a new node with that value to the back of the queue with an O(1) Time performance.

- dequeue
Arguments: none
Returns: the value from node from the front of the queue
Removes the node from the front of the queue
Should raise exception when called on empty queue

- peek
Arguments: none
Returns: Value of the node located at the front of the queue
Should raise exception when called on empty stack

- is_empty
Arguments: none
Returns: Boolean indicating whether or not the queue is empty
