class student:
    student ="Gopikrishna"
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()

    def show(self):
        print(self.name,self.rollno,self.lap)
        self.lap.show()
    class laptop:
        def __init__(self):
            self.brand="Lenovo"
            self.cpu="I5"
            self.ram=8
        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = student("Navin",2)
s2 = student("Sai",22)

s2.show()