# array = ["hey", "bro", "you'r", "awesom"]
# itr = iter(array)
# itr
# print(next(itr))
# print(next(itr))

# # Iterator in Reversed Mood
# itr = reversed(array)
# print(next(itr))

class RemoteControl():
    def __init__(self):
        self.channels = ["HBO", "cnn", "abc", "espn"]
        self.index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        
        return self.channels[self.index]
    
r = RemoteControl()
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
