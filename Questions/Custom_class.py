# Topic: Custom Classes in Python

# Description: You are tasked with creating a Rectangle class with the following requirements:

# An instance of the Rectangle class requires length:int and width:int to be initialized.
# We can iterate over an instance of the Rectangle class 
# When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}



class Rectangle:
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def __iter__(self):
        yield f'length: {self.length}'
        yield f'width: {self.width}'
        
  
    def area(self):
        return self.width * self.length

    
    



r=Rectangle(5, 10)

for i in r:
    print(i)
    
# output:
#     5
#     10