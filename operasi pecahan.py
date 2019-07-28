class pecahan():
    def __init__(self,a,b,c):
        self.bulat = a
        self.pemb = b
        self.peny = c

        if (self.bulat == 0):
            self.pemb2 =  self.pemb
            print(self.pemb,"/",self.peny)

        else :
            self.pemb2 = self.bulat*self.peny + self.pemb
            print(self.bulat,self.pemb,"/",self.peny)
    # mencari fpb dengan metode rekursif(algoritma euclidean)    
    def gcd(self,a,b):
        if (a == 0):
            return b
        return self.gcd(b%a,a)
    def lcm(self,a,b):
        fpb = self.gcd(a,b)
        lcm = (a*b)/fpb
        return lcm
    
    def kali (self,a):
        x = self.pemb2 * a.pemb2
        y = self.peny * a.peny

        print ("hasil kali =", x,"/",y)

    def bagi (self, a):
        x = self.pemb2*a.peny
        y = self.peny*a.pemb2
        print("hasil bagi =", x,"/",y)
    
    def tambah(self,a):
        x = self.gcd(self.peny, a.peny)
        y = self.lcm(self.peny,a.peny)
        z = ((y/self.peny)*self.pemb2) + ((y/a.peny)*a.pemb2)
        print("hasil tambah = ",z,"/",y )
    def kurang(self,a):
        x = self.gcd(self.peny, a.peny)
        y = self.lcm(self.peny,a.peny)
        z = ((y/self.peny)*self.pemb2) - ((y/a.peny)*a.pemb2)
        print("hasil tambah = ",z,"/",y )

a = pecahan(2,2,3)
b = pecahan(0,1,4)
a.kali(b)
a.bagi(b)
a.tambah(b)
a.kurang(b)

        

