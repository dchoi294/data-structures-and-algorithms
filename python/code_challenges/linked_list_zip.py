from data_structures.linked_list import LinkedList


def zip_lists(a, b):
    new_list = LinkedList()

    while a.head or b.head:

        if a.head:
            new_list.append(a.head.value)
            a.head = a.head.next

        if b.head:
            new_list.append(b.head.value)
            b.head = b.head.next

    return new_list
