class Circular:
    def __init__(self, sequence, direction=1, origin=0):
        self.seq = sequence
        self.direction = direction
        self.origin = origin

    def __getitem__(self, arg):
        return self.seq[arg]

    # return sum of naive slices

    def __iter__(self):
        return self.islice()

    def __eq__(self, other):
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __len__(self, n):
        return len(self.seq)

    def gap(self, start, stop):
        # completes orbits
        return stop, start - len(self)

    def partition(self, slice1):
        pass

    def islice(self, start, stop):
        return iter(self[start:stop])

    def cycle(self, start):
        pass

    def index(self, element):
        pass

    def reverse(self):
        self.direction *= -1

    def rotate(self, steps):
        self.origin -= steps
