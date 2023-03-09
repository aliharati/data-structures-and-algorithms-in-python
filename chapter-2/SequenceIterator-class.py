class SequenceIterator:
    """An iterator for any Python's sequence type."""

    def __init__(self, sequence):
        """Create an iterator for the given sequence"""
        self._seq = sequence
        self._k = -1   # will increment to 0 on first call to next
    
    def __getitem__(self, item):
        return self._seq[item]
    
    def __next__(self):
        """Return the next element, or else raise StopIteration error"""
        self._k += 1
        if self._k < len(self._seq):
             return self[self._k]
        else:
            raise StopIteration()
    def __iter__(self):
        """By convention, an iterator must return itself as an iterator"""
        return self
    
x = iter([1,2,3,4,5,6])
print(next(x))
print(next(x))
print(next(x))
print()
for s in x:
    print(s)
print()
x = SequenceIterator([1,2,3,4,5,6])
print(next(x))
print(next(x))
print(next(x))
print(list(x)) #this works because of the __iter__(self) method