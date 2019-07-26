class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    def set_data(self,data):
        self.data = data
    def get_data(self):
        return self.data
    def set_next(self,data):
        self.next = data
    def get_next(self):
        return self.next

class Linked():
    def __init__(self):
        self.size = 0
        self.head = None
    
    def Addfirst(self,node):
        newnode = node
        newnode.next = self.head
        self.head = newnode
        self.size += 1
    
    def printall (self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
        
    def sort (self):
        if self.size > 1:
            newlist = []
            current = self.head
            newlist.append(self.head)
            while current.next != None :
                current = current.get_next()
                newlist.append(current)
            listInteger = []
            for i in newlist:
                listInteger.append(i.get_data())
            listInteger = sorted(listInteger)
            
            Rafid = Linked()
            for i in listInteger:
                Rafid.Addfirst(Node(i))
            self.head = Rafid.head
        return self
        
if __name__== "__main__" :
    node1 = Node(3)    
    node2 = Node(2)
    node3 = Node(9)
    node4 = Node(6)

    Rafid = Linked()
    Rafid.Addfirst(node1)
    Rafid.Addfirst(node2)
    Rafid.Addfirst(node3)
    Rafid.Addfirst(node4)
    Rafid.printall()
    print ("-----")
    Rafid.sort()
    Rafid.printall()

    
        
        




