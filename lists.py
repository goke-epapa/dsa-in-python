class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position. Assume the first position is "1".
        Return "None" if position is not in the list."""
        index = 0
        curr = self.head
        while index < position:
            index = index + 1
            if curr is None:
                return None

            if index == position:
                return curr
            else:
                curr = curr.next
        return None

    def delete(self, value):
        """Delete the first node with a given value."""
        curr = self.head

        if curr:
            if curr.value == value:
                self.head = curr.next
            else:
                while curr.next:
                    if curr.next.value == value:
                        curr.next = curr.next.next
                    else:
                        curr = curr.next
        pass

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""

        if position < 1:
            pass

        curr = self.head
        if position == 1:
            new_element.next = curr
            self.head = new_element

        index = 1
        if curr.next:
            while index <= position:
                next_elem = curr.next
                index = index + 1
                if index == position:
                    new_element.next = next_elem
                    curr.next = new_element
                else:
                    curr = curr.next

                if curr is None:
                    break
        pass

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        curr = self.head
        new_element.next = curr
        self.head = new_element
        pass

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        curr = self.head
        if curr:
            self.head = curr.next
        return curr


class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)
        pass

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()


if __name__ == '__main__':
    elem = Element(5)
    ll = LinkedList(elem)

    ll.append(Element(5))
    ll.append(Element(10))
    ll.append(Element(11))

    ll.delete(5)
    ll.insert(Element(11), 4)

    current = ll.head
    while current:
        print current.value
        current = current.next

    # elem = ll.get_position(4)
    # print elem
