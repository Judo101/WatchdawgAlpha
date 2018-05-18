class Resolution(object):
    def __init__(self, resolutionx, resolutiony, size, position):
        self.resolution = resolution
        self.size = size
        self.position  = position

    @property
    def resolutionx(self):
        return self._resolutionx
    @resolutionx.setter
    def resolutionx(self, resolutionx):
        self._resolutionx = resolutionx

    @property
    def resolutiony(self):
        return self._resolutiony
    @resolutiony.setter
    def resolutiony(self, resolutiony):
        self._resolutiony = resolutiony

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self._size = size

    @property
    def position(self):
        return self._position
    @position.setter
    def position(self, position):
        self._position = position

class Res1(Resolution):
    def __init__(self):
        Resolution.__init__(self, 1280, 720, '32', '+1100+700')

class Res2(Resolution):
    def __init__(self):
        Resolution.__init__(self, 1366, 768, '32', '+1170+750')

class Res3(Resolution):
    def __init__(self):
        Resolution.__init__(self, 1600, 900, '32', '+1450+7885')

class Res4(Resolution):
    def __init__(self):
        Resolution.__init__(self, 1920, 1080, '40', '+1950+1050')

class Res5(Resolution):
    def __init__(self):
        Resolution.__init__(self, 1920, 1200, '40', '+1750+1180')

class Res6(Resolution):
    def __init__(self):
        Resolution.__init__(self, 2560, 1440, '64', '+2280+1400')

class Res7(Resolution):
    def __init__(self):
        Resolution.__init__(self, 2560, 1600, '64', '+2240+1550')

class Res8(Resolution):
    def __init__(self):
        Resolution.__init__(self, 2592, 1944, '64', '+2300+1890')
