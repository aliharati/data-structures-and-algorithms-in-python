class Vector:
    """A multi dimentional vector"""

    def __init__(self,dimentions):
        self._coords = []
        self._n = 0
        for i in range(dimentions):
            self._coords.append(0)
    
    def __len__(self):
        return len(self._coords)
    
    def __getitem__(self, item):
        return self._coords[item]

    def __setitem__(self, item, value):
        self._coords[item] = value
    
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimentions must agree')
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result
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
    print(v[4]) # print 45 (via getitem )
    u = v + v # <0, 46, 0, 0, 90> (via add )
    print(u) # print <0, 46, 0, 0, 90>
    total = 0
    for entry in v: # implicit iteration via len and getitem
        total += entry
    print(total)


    