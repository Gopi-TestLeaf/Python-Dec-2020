class Hospital:

    classVariable = 10

    def __init__(self, x):
        self.x = x

    def adm(self):
        print('adm - self')

    @classmethod
    def informPolice(cls):
        print('informing to police')

    @staticmethod
    def healthCheckup():
        pass

