class Mobil:

    def __init__(self,merk):
        self._merk = merk

sedan = Mobil('Toyota')
print(f'Merk : {sedan._merk}')