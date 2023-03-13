class Range:
    """A multi dimentional vector"""

    def __init__(self, start, stop=None, step=1):

        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:
            start, stop = 0, start
        
        self._start = start
        self._stop = stop
        self._step = step
        
        if step > 0:
            self._length = max(0,(stop - start + step - 1) // step)
        else:
            self._length = max(0,(stop - start + step + 1) // step)  #correction

    def __len__(self):
        return self._length

    def __getitem__(self,item):
        if item > len(self):
            raise IndexError('item is out of range')
        else:
            return self._start + (self._step * item)    




if __name__ == '__main__':

    x = Range(-10,1,2)
    print(len(x))
    print(len(range(-10,1,2)))
    print(x[5])

    s = Range(1,-10,-3)
    print(len(s))
    print(len(range(1,-10,-3)))
    print(s[4])