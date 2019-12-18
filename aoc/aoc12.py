class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"<x={self.x:3d}, y={self.y:3d}, z={self.z:3d}>"

    def __iter__(self):
        for i in [self.x, self.y, self.z]:
            yield i


class Moon:
    def __init__(self, position: Vector, velocity: Vector):
        self.position = position
        self.velocity = velocity

    def __repr__(self):
        return f"pos={self.position}, vel={self.velocity}"

    def kinetic(self):
        return sum(map(abs, self.velocity))

    def potential(self):
        return sum(map(abs, self.position))

    def total(self):
        return self.kinetic() * self.potential()


class Jupiter:
    def __init__(self, moons):
        self.moons = moons

    def potential(self):
        return

    def kinetic(self):
        return 0

    def total(self):
        return self.potential * self.kinetic


p = Vector(2, 2, -2)
v = Vector(-1, -1, 1)
moon = Moon(position=p, velocity=v)


def test_moon_kinetic():
    assert moon.kinetic() == 3

def test_moon_potential():
    assert moon.potential() == 6

def test_moon_total():
    assert moon.total() == 18



def main():
    pass


if __name__ == '__main__':
    main()
