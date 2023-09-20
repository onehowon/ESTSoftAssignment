class A:
    def hello(self):
        print('hello A')

class B:
    def hello(self):
        print('hello B')

class C(A):
    def hello(self):
        print('hello C')

class D(B, C):
    pass

d = D()
d.hello()
