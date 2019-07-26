class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Circular:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        new = Node(data)
        temp = self.head
        new.next = self.head

        if self.head is not None :
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new

        else :
            new.next = new
        
        self.head = new

    def print(self):
        temp = self.head
        if self.head is not None :
            while(True):
                print(temp.data)
                temp = temp.next
                if (temp == self.head):
                    break


rafid = Circular()
rafid.push (2)
rafid.push (5)
rafid.push (6)
rafid.push (9)
rafid.print()

