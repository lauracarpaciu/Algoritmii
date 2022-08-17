class MyQueue:
    def __init__(self, storage, tail,head):
        self.storage = storage
        self.tail = tail
        self.head = head

    def enqueue(self,element):
        self.tail +=1
        self.storage[self.tail]=element


    def dequeue(self, element):
        if self.isEmpty() :
            return None

        element = self.storage[self.head]

        self.head +=1

        return  element



    def isEmpty(self):
        if self.storage[self.tail]<self.storage[self.head]:
            return self.tail<self.head


myqueue = MyQueue(storage=[],tail=0,head =1)

myqueue.enqueue("Ion")
myqueue.enqueue("George")
myqueue.enqueue("Mihai")
next = myqueue.dequeue()
print(next)