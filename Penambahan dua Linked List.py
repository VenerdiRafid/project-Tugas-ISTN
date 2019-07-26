class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList :
    def __init__(self):
        self.head = None
    
    def push(self, data):
        new  = Node(data)
        new.next = self.head
        self.head = new
    
    def printlist(self):
        temp = self.head
        while (temp is not None):
            print (temp.data)
            temp = temp.next
        
    def sum(self, B):
        temp = self.head
        temp2 = B.head
        a = []
        b = []

        while(temp is not None):
            a.append(temp.data)
            temp = temp.next
       
        while(temp2 is not None):
            b.append(temp2.data)
            temp2 = temp2.next

        c = []
        d = []

        if len(a) > len (b):
            for i in range (len(a)):
                m = a[len(a)-i-1]
                n = b[len(b)-i-1]
                c.append(m+n)
        else :
            for i in range (len(b)):
                m = a[len(a)-i-1]
                n = b[len(b)-i-1]
                c.append(m+n)
            
        next = False
        for i in range(len(c)):
            p = c[i]
            if next == True:
                p += 1
                if p < 10:
                    next == False
            if p >= 10:
                p = p-10
                next = True
            d.append(p)

        rafid =  LinkedList()
        for i in range (len (d)):
            rafid.push(d[i])

        print("hasil penjumlahan :")
        rafid.printlist()


a = LinkedList()
b = LinkedList()

a.push(4)
a.push(3)
a.push(2)
a.push(1)
print ("ini Linked List a :")
a.printlist()
b.push(5)
b.push(4)
b.push(3)
b.push(2)
print("ini Linked List b :") 
b.printlist()
a.sum(b)




            
        


        