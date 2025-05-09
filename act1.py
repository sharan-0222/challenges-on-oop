class a:
    def __init__(self,a):
        self.a=a

    def __lt__(self,other):
        if (self.a<other.a):
            print("a is less than b")
        else:
            print("a is greater than b")

    def __eq__(self,other):
        if (self.a==other.a):
            print("a is equal to b")
        else:
            print("a is not equal to b")

obj1=a(99)
obj2=a(10000)
print(obj1<obj2)

obj3=a(12)
obj4=a(12)
print(obj3==obj4)    