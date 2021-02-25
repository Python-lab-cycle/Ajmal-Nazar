class time:
    #defining init method for class
    def __init__(self,h,m):
        self.hr=h
        self.min=m
    #overloading the less than operator using special function
    def __add__(self,other):
        self.hr=self.hr+other.hr
        self.min=self.min+other.min
        return time(self.hr,self.min)
    #string function to print object of complex class
    def __str__(self):
        return str(self.hr)+'hr'+str(self.min)+'min'
t1=time(5,3)
t2=time(2,4)
print(t1+t2)
