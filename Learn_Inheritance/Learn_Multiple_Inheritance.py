class GA:

    def same(self):
        print("My name is Same, i'm coming from GA")

class A(GA):

    def a(self):
        print("I'm from Class A")


class B:

    def same(self):
        print("My name is Same, i'm coming from B")

    def b(self):
        print("I'm from Class B")


class C(A, B):

    def c(self):
        print("I'm from Class C")


cc = C()



