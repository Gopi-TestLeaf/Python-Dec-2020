class TestLeaf:

    tl_pho = 123456789
    gopi_office = 90909
    _gopi_per = 100          # Data Hiding

    def _someFun(self):
        print('sf')

    def python(self):
        print('python for Dev and DS')

    def get_data(self):
        return TestLeaf._gopi_per


    def set_data(self, new_ph):
        TestLeaf._gopi_per = new_ph


x = TestLeaf()
print(x.get_data())
x.set_data(200)
print(x.get_data())

