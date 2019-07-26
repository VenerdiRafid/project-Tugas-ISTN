class kalender:
    def  getdata(self):
        self.d = int(input('masukkan hari = \n'))
        self.m = int(input('masukkan bulan = \n'))
        self.y = int(input('masukkan tahun  = \n'))

    def putdata(self):
        if self.m == 1:
            self.hari = 31
            self.bulan = 'Januari'
        elif self.m == 2:
            if (self.y % 4 == 0):
                if (self.y % 100 == 0):
                    if (self.y % 400 == 0):
                        self.hari = 29
                    else :
                        self.hari = 28
                else :
                        self.hari = 28
            else :
                        self.hari = 28
            self.bulan = "februari"
        elif self.m == 3 :
            self.hari = 31
            self.bulan = 'maret'
       
        elif self.m == 4 :
            self.hari = 30
            self.bulan = 'april'
        elif self.m == 5 :
            self.hari = 31
            self.bulan = 'mei'
        elif self.m == 6 :
            self.hari = 30
            self.bulan = 'juni'
        elif self.m == 7 :
            self.hari = 31
            self.bulan = 'juli'
        elif self.m == 8 :
            self.hari = 31
            self.bulan = 'agustus'
        elif self.m == 9 :
            self.hari = 30
            self.bulan = 'september'
        elif self.m == 10 :
            self.hari = 31
            self.bulan = 'oktober'
        elif self.m == 11 :
            self.hari = 30
            self.bulan = 'november'
        elif self.m == 12 :
            self.hari = 31
            self.bulan = 'desember'
        
        else :
            self.hari = self.d
            self.bulan = self.m

    def printdata(self):
        dvalid = self.d >= 1 and self.d <= self.hari
        mvalid = self.m >= 1 and self.m <= 12
        valid = dvalid and mvalid
        if (valid) :
            print (self.d,self.bulan,self.y)
        
        else :
            print('invalid : Masukan kembali ! \\n')
        
         
        
            
data = kalender ()
data.getdata()
data.putdata()
data.printdata()
        

           

                