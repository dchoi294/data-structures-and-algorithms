## Challenge

Write a function called fizz buzz tree that determine whether or not the value of each node is divisible by 3, 5 or both.

## Whiteboard Process

![Whiteboard](whiteboard.png)

## Approach & Efficiency

- Create a copy of the input tree using copy.deepcopy()
- If the value is divisible by 3, replace the value with “Fizz”
- If the value is divisible by 5, replace the value with “Buzz”
- If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
- If the value is not divisible by 3 or 5, simply turn the number into a String.
- If the node has children, start a call stack of the helper function, passing in the children nodes from left to right, which will return each node until the whole tree has been traversed. .
- Return the copied tree


***Big O***
Time: O(n) - will take linear depending on the size of the tree
Space: O(1) - constant space because there is no variable that is dependent on the size of the input

## API

- pip install pytest
- ran tests based on the tests given and all passed
