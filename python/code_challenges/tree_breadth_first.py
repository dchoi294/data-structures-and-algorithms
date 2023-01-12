from data_structures.queue import Queue


def breadth_first(tree):
    result = []
    if not tree.root:
        return result
    queue = Queue()
    queue.enqueue(tree.root)
    while queue.front:
        front = queue.dequeue()
        result.append(front.value)
        if front.left:
            queue.enqueue(front.left)
        if front.right:
            queue.enqueue(front.right)
    return result
