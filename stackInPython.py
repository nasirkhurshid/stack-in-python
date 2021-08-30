'''
Created on Aug 28, 2021.
@author: Nasir Khurshid
All right reserved.
'''

class stack:
    size = 0
    top = 0
    st = [0]

    def __init__(self, s):
        self.size=s;
        self.top=0;
        self.st=[0]

    def push(self, val):
        if self.top==0:
            self.st.pop()
        self.st.insert(self.top, val)
        self.top+=1
        
    def pop(self):
        self.top-=1
        
    def Top(self):
        return self.st[self.top-1]
    
    def empty(self):
        return self.top==0
    
    def makeempty(self):
        self.top=0
        
    def full(self):
        return self.top==self.size
    
    def Size(self):
        return self.top
    
    
'''Client Code'''
   
s = stack(3)
s.push(3)
s.push(5)
s.push(7)

print("Size of Stack: ", end="")
print(s.Size())
print("Is stack full? ", end='')
print(s.full())

print("Displaying values of Stack:")
for x in range(s.Size()):
    print(s.Top())
    s.pop()

print("Size of Stack: ", end="")
print(s.Size())
print("Is stack full? ", end='')
print(s.full())

s.push(2)
s.push(4)
s.push(6)

print("Displaying values of Stack:")
for x in range(s.Size()):
    print(s.Top())
    s.pop()

#code for checking makeempty function
#s.push(77)
    
if s.empty() is False:
    print("Making Stack empty...")
    s.makeempty()
    if s.empty():
        print("Stack emptied successfully!")
    else:
        print("Stack could not be emptied!")
else:
    print("Stack is already empty!")
