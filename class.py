#__init__ = function that creates a point
# self = object that is created from __init__ to store the inputs
# inputx, inputy = properties that store inputs to be used/retured when needed
 
class point():
    def __init__(self, inputx, inputy):
        self.x = inputx
        self.y = inputy
        
p = point(2, 8)
print(p.x)
print(p.y)

class flight():