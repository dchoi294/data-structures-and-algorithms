# Challenge Summary
Creating a method called kth_from_end
argument: a number, k, as a parameter.
Return the node¡¯s value that is k places from the tail of the linked list.
You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Whiteboard Process

![whiteboard](CC07%20whiteboard.png)

## Approach & Efficiency

- If k is less than 0, Exception
- Setting current = self.head
- A empty list to append the value of current into it. (Using while loop to append)
- Setting current = current.next inside while loop (to continue the loop)
- Returns list[-k-1] when the while loops ends
- try and except to raise Exception if it happens (TargetError())

## Solution

Installed and used pytest.
- All tests have passed.
