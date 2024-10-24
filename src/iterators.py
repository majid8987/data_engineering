class NumberIterator:
    def __init__(self,start,end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.end :
            result = self.current
            self.current +=1
            return result
        else:
            raise StopIteration


num_iterators = NumberIterator(1,6)

for i in num_iterators:
    print(i)
