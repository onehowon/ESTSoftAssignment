
class A:

    def one(self):
        return 'one'

class B(A):
    def two(self):
        return 'two'

class C(B):
    def three(self):
        return 'three'

c = C()
c.one()
c.two()
c.three()
     