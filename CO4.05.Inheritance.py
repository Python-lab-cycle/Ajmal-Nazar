class publisher:
    def __init__(self,pname):
        self.pname=pname
    def display(self):
        print("Pname",self.pname)
class book(publisher):
    def __init__(self,pname,bname,author):
        self.pname=pname
        self.bname=bname
        self.author=author
    def display(self):
        print("Pname",self.pname)
        print("Bname",self.bname)
        print("Author",self.author)
class python(book):
    def __init__(self,pname,bname,author,page,price):
        self.pname=pname
        self.bname=bname
        self.author=author
        self.page=page
        self.price=price
    def display(self):
        print("Publisher Name",self.pname)
        print("Book Name",self.bname)
        print("Author",self.author)
        print("Page",self.page)
        print("Price",self.price)

n=input("Enter publisher:")
b=input("Enter book:")
t=input("Enter author:")
p=input("Enter page:")
pr=input("Enter price:")
obj=python(n,b,t,p,pr)
obj.display()
        
