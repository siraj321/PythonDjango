class Vector:
    def __init__(self, a, b):
        print("init...");
        self.a = a
        self.b = b

    def __str__(self):
        print("str...")
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self,other):
        print("add...")
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
v3 = Vector(1,1)
print (v1 + v2 +v3)