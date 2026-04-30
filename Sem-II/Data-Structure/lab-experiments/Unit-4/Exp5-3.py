class MinHeap:
    def __init__(self):
        self.h = []

    def insert(self, x):
        self.h.append(x)
        self._up(len(self.h) - 1)

    def peek(self):
        return self.h[0] if self.h else None

    def extract(self):
        if not self.h:
            return None
        if len(self.h) == 1:
            return self.h.pop()
        root = self.h[0]
        self.h[0] = self.h.pop()
        self._down(0)
        return root

    def _up(self, i):
        while i > 0:
            p = (i - 1) // 2
            if self.h[p] <= self.h[i]:
                break
            self.h[p], self.h[i] = self.h[i], self.h[p]
            i = p

    def _down(self, i):
        n = len(self.h)
        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            s = i
            if l < n and self.h[l] < self.h[s]:
                s = l
            if r < n and self.h[r] < self.h[s]:
                s = r
            if s == i:
                break
            self.h[i], self.h[s] = self.h[s], self.h[i]
            i = s


class MaxHeap:
    def __init__(self):
        self.h = []

    def insert(self, x):
        self.h.append(x)
        self._up(len(self.h) - 1)

    def peek(self):
        return self.h[0] if self.h else None

    def extract(self):
        if not self.h:
            return None
        if len(self.h) == 1:
            return self.h.pop()
        root = self.h[0]
        self.h[0] = self.h.pop()
        self._down(0)
        return root

    def _up(self, i):
        while i > 0:
            p = (i - 1) // 2
            if self.h[p] >= self.h[i]:
                break
            self.h[p], self.h[i] = self.h[i], self.h[p]
            i = p

    def _down(self, i):
        n = len(self.h)
        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            s = i
            if l < n and self.h[l] > self.h[s]:
                s = l
            if r < n and self.h[r] > self.h[s]:
                s = r
            if s == i:
                break
            self.h[i], self.h[s] = self.h[s], self.h[i]
            i = s


def run(priorities):
    mh = MinHeap()
    xh = MaxHeap()
    for p in priorities:
        mh.insert(p)
        xh.insert(p)
    min_seq = []
    min_states = []
    while mh.peek() is not None:
        min_seq.append(mh.extract())
        min_states.append(mh.h.copy())
    max_seq = []
    max_states = []
    while xh.peek() is not None:
        max_seq.append(xh.extract())
        max_states.append(xh.h.copy())
    return {
        "min_extracted": min_seq,
        "min_states": min_states,
        "max_extracted": max_seq,
        "max_states": max_states
    }


if __name__ == "__main__":
    import sys
    data = list(map(int, sys.stdin.read().strip().split()))
    out = run(data)
    print(out["min_extracted"])
    for s in out["min_states"]:
        print(s)
    print(out["max_extracted"])
    for s in out["max_states"]:
        print(s)