# Challenge Summary

- Create a new class called pseudo queue.
- Do not use an existing Queue.
- Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below),
- Internally, utilize 2 Stack instances to create and manage the queue

Methods:

***enqueue***
- Arguments: value
- Inserts a value into the PseudoQueue, using a first-in, first-out approach.
***dequeue***
- Arguments: none
- Extracts a value from the PseudoQueue, using a first-in, first-out approach.

## Whiteboard Process

![whiteboard](CC11%20whiteboard.png)

## Approach & Efficiency

- Instances creates two empty Stack instances as properties: Stack1, Stack2

- Create enqueue method that pops all  items from stack2 and push it to stack1, then pushes input value to stack1

- Create dequeue method that pops all items from stack1 and push it to stack2, then return the top value from stack2.

## Solution

Installed and used pytest.
- All tests have passed.

![code](../../code_challenges/stack_queue_pseudo.py)
