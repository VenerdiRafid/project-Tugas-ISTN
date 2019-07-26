class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLink:
    def __init__(self):
        self.head = None
    def push(self,data):
        newdata = Node(data)
        newdata.next = self.head

        if self.head is not None :
            self.head.prev = newdata
            
        self.head = newdata
    def InsertAfter(self,prev_data,data):
        if prev_data is None :
            print ('masukkan prev data')
            return
        newdata = Node(data)
        newdata.next = prev_data.next
        prev_data.next = newdata
        newdata.prev = prev_data
        if newdata.next is not None :
            newdata.next.prev = newdata
    def append(self, data):
        newdata = Node(data)
        newdata.next = None
        if self.head is None:
            newdata.prev = None
            self.head = newdata
            return
        
        last = self.head
        while(last.next is not None):
            last = last.next
        
        last.next = newdata
        newdata.prev = last
        return
    def print(self, node):
        print("print data in forward direction")
        while(node is not None):
            print(node.data)
            last = node
            node = node.next

        print ("print data in revese direction")
        while (last is not None):
            print(last.data)
            last = last.prev


rafid = DoubleLink()
rafid.push(4)
rafid.push(2)
rafid.InsertAfter(rafid.head.next, 5)
rafid.append(7)
rafid.print(rafid.head)
    
        
    


    

