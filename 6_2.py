class Road:
    _gravity: int = 5

    def __init__(self, length: [int], width: [int]):
        self._length = int(length)
        self._width = int(width)

    def get_surface_gravity(self, thicknes: int) -> [int, None]:
     return (self._length * self._width * thicknes * self._gravity)

if __name__:
 road = Road(5000, 10)
print( 'Масса дорожного покрытия составит:', road.get_surface_gravity(20),'тонн')
