class A:

    def a(self):
        print('Hello')


class B(A):

    def a(self):
        print('Hello every')

    def b(self):
        print('Hi')

x = B()
x.a()