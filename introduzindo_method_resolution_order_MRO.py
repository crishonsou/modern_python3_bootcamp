class A:
    def do_something(self):
        print('Method defined in: A')

class B(A):
    def do_something(self):
        print('Method defined in: B')
        super().do_something()


class C(A):
    def do_something(self):
        print('Method defined in: C')



class D(B,C):
    def do_something(self):
        print('Method defined in: A')
        super().do_something()




# Method resolution order:
# |      D
# |      B
# |      C
# |      A
# |      builtins.object

thing = D()
#print(D.__mro__)
#print(D.mro())
#help(D)
thing.do_something()

