

class Vector:
    """A multi dimentional vector"""

    def __init__(self,dimensions):
        
        self._n = 0
        if isinstance(dimensions,int): # R-2.15
            self._coords = []
            for i in range(dimensions):
                self._coords.append(0)
        else:
            self._coords = dimensions
    
    def __len__(self):
        return len(self._coords)
    
    def __getitem__(self, item):
        return self._coords[item]

    def __setitem__(self, item, value):
        self._coords[item] = value
    
    def __neg__(self):                      # R-2.10
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = -self[i]
        return result
    
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result
    
    def __radd__(self, other):              # R-2.11
        return self + other
    
    def __sub__(self, other):               # R-2.9
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] - other[i]
        return result
    
    def __mul__(self, other):              # R-2.12 & R-2.14
        result = Vector(len(self))

        for i in range(len(self)):
            if isinstance(other,(int,float)):
                result[i] = self[i] * other
            else: 
                if len(other) != len(self):
                    raise ValueError('dimension must agree')
                for i in range(len(self)):
                    result[i] = self[i] * other[i]
        return result
    
    def __rmul__(self,amount):              # R-2.13
        return self * amount
    
    def __eq__(self, other):
        return self._coords == other._coords
    
    def __ne__(self, other):
        return self._coords != other._coords
    
    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

if __name__ == '__main__':
    v = Vector(5) # construct five-dimensional <0, 0, 0, 0, 0>
    v[1] = 23 # <0, 23, 0, 0, 0> (based on use of setitem )
    v[-1] = 45 # <0, 23, 0, 0, 45> (also via setitem )
    print("v[4]: ",v[4]) # print 45 (via getitem )
    u = v + v # <0, 46, 0, 0, 90> (via add )
    print("u: ",u) # print <0, 46, 0, 0, 90>
    x = u - v
    print("x: ",x)
    n = -x
    print("n: ",n)
    total = 0
    s = n + [5, 3, 10, -2, 1]
    print("s: ", s)
    d = [5, 3, 10, -2, 1] + s
    print("d: ",d)
    b = d * 3
    print("b: ",b)
    p = 3 * b
    print("p: ",p)
    m = p * v
    print("m: ",m)
    l = Vector([1,2,3,4])
    print("l: ",l)
    for entry in v: # implicit iteration via len and getitem
        total += entry
    print(total)

    