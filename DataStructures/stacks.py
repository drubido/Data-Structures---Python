# Stack class
# From this class we want to be able to perform basic stack operations
# Such as creating a stack, checking if stack is empty, adding items to stack,
# Eliminating the first Item in the stack, checking last item in the stack, count items in stack.

# Carlos D. Rubido Rafull 

class Stack:
    # Create stack
    def __init__(self):
        self.items = []

    # Check if stack is empty
    def isEmpty(self):
        return self.items == []

    # Add item to stack
    def push(self, item):
        self.items.append(item)

    # Eliminate first item in the stack
    def pop(self):
        return self.items.pop()

    # Access last item in the stack
    def peek(self):
        return self.items[len(self.items)-1]

    # Get the size of my stack
    def size(self):
        return len(self.items)