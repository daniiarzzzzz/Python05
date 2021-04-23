l = [1, 2, 3, 4, 5, 6, 7]


class Ochered:

    def __init__(self, q):
        self._q = q

    def pop(self):
        return self._q.pop(0)

    def append(self, item):
        self._q.append(item)

    @property
    def q(self):
        return "Ochered ->", self._q


ochered = Ochered(l)
print(ochered.q)
ochered.append(8)
ochered.append(9)
ochered.append(10)
print(ochered.q)
ochered.pop()
ochered.pop()
print(ochered.q)
