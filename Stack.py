# package samples

# Python program to demonstrate stack implementation using a linked list.

# Class representing one position in the stack; only used internally
class Stack:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    # Initializing a stack.
    def __init__(self):
        self.head = None  # Node("head")
        self.size = 0

    # String representation of the stack, for printouts
    def __str__(self):
        cur = self.head
        out = ""
        while cur is not None:
            out += str(cur.value) + "->"
            cur = cur.next
        return "[ " + out[:-2] + " ]"

    # Get the current size of the stack
    def get_size(self):
        return self.size

    # Check if the stack is empty
    def is_empty(self):
        return self.size == 0

    # Get the top item of the stack, without removing it
    def peek(self):
        if self.is_empty():
            raise ValueError("Peeking from an empty stack")
        return self.head.next.value

    # Push a value onto the stack
    def push(self, value):
        new_node = Stack.Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    # Remove a value from the stack and return it
    def pop(self):
        if self.is_empty():
            raise ValueError("Popping from an empty stack")
        node_to_pop = self.head
        self.head = self.head.next
        self.size -= 1
        return node_to_pop.value

    # Remove all elements from the stack
    def clear(self):
        self.head = None
        self.size = 0
    
    def BottomInsert(self, value):
    # if stack is empty then call push() method.
        if self.is_empty():  
            self.push(value)
            
        # if stack is not empty then execute else
        # block
        else:
        
            # remove the element and store it to
            # popped  
            popped = self.pop()
            
            # invoke it self and pass stack and value 
            # as an argument.
            self.BottomInsert(value)
            
            # append popped item in the bottom of the stack 
            self.push(popped)

    def reversee(self): 

        # check the stack is empty of not  
        if self.is_empty():
        
            # if empty then do nothing
            pass
            
        # if stack is not empty then 
        else:
        
            # pop element and stare it to popped
            popped = self.pop()
            
            # call it self ans pass stack as an argument
            self.reversee()
            
            # call BottomInsert() method and pass stack
            # and popped element as an argument
            self.BottomInsert(popped)

# TODO Possibly more methods

def test():

    """stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")
    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")
"""

# Driver Code
if __name__ == "__main__":
    test()
