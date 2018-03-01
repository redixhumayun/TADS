import sys
sys.path.append('/Users/zaidhumayun/Desktop/Development/Python/ctci/Stacks')
from stack import Stack

class Parenthesis():
    def __init__(self, string):
        self.string = string
        self.stack = Stack()

    def check(self):
        for char in self.string:
            if char == '(':
                self.stack.push(char)
            elif char == ')':
                if self.stack.pop() == -1:
                    return False
        return True
    
if __name__ == "__main__":
    p = Parenthesis("(())")
    print(p.check())
        