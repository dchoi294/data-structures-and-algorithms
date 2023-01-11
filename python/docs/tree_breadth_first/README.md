## Challenge

Write a function called breadth first
Arguments: tree
Return: list of all values in the tree, in the order they were encountered

## Whiteboard Process

![Whiteboard](whiteboard.png)

## Approach & Efficiency

Make an empty list and a queue with the input tree's root node.
Make a while loop to pop off the front of the queue and append the value of front to the list.
Continue it until the queue is empty.

***Big O***
Time: O(n) - will take linear depending on the size of the input
Space: O(n) - list will grow linearly depending on the size of the input

## API

- pip install pytest
- ran tests based on the tests given and all passed
