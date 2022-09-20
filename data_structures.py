class myStack:
    def __init__(self):
        self.stk = []
    def push(self, value):
        self.stk.append(value)
    def pop(self):
        to_remove = self.stk[len(self.stk) - 1]
        self.stk.remove(to_remove)
        return to_remove
    def peek(self):
        return self.stk[len(self.stk) - 1]
    def isEmpty(self):
        return len(self.stk) == 0

class myQueue:
    def __init__(self):
        self.q = []
    def enqueue(self, value):
        self.q.append(value)
    def dequeue(self):
        to_remove = self.q[0]
        self.q.remove(to_remove)
        return to_remove
    def peek(self):
        return self.q[0]
    def isEmpty(self):
        return len(self.q) == 0

class myLinkedList:
    def __init__(self):
        self.head = None
    def add(self, node):
        if(self.head is None):
            self.head = node
        else:
            current = self.head
            while(current.next is not None):
                current = current.next
            current.next = node
    def format_list(self):
        if(self.head == None):
            return 'Empty list...'
        else:
            current = self.head
            str = ''
            while(current is not None):
                str += f'{current.data}\n'
                current = current.next
            return str
class myNode:
    def __init__(self, data=None):
        if(data is None):
            self.data = None
        self.data = data
        self.next = None




