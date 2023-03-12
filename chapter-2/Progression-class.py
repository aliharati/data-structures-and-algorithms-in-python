class Progression:
    """a class for iterating by specific mesures"""

    def __init__(self, start=0):
        
        self._current = start
    
    def _advance(self):

        self._current += 1
    
    def __next__(self):

        if self._current is None:
            raise StopIteration
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):

        return self
    
    def print_progression(self, n):

        print(''.join(str(next(self)) for i in range(n)))
        

class ArithmeticProgression(Progression):
    def __init__(self, incriment= 1, start = 0):

        super().__init__(start)
        self._incriment = incriment
    
    def _advance(self):
        
        self._current += self._incriment


class GeometricProgression(Progression):

    def __init__(self, base=2, start=1):
        
        super().__init__(start)
        self._base = base
    
    def _advance(self):
        self._current *= self._base

class FibonacciProgression(Progression):

    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first
    def _advance(self):
        self._prev, self._current = self._current, self._current + self._prev
    
                


if __name__ == "__main__":
    

    x = Progression()

    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print()

    x = ArithmeticProgression()

    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print()

    x = GeometricProgression()

    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print()
    
    x = FibonacciProgression(2,3)

    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print()