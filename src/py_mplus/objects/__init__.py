from abc import abstractmethod


class MPData:
    def __init__(self, buffer):
        self.buffer = buffer
        self.pos = 0

    def __len__(self):
        return len(self.buffer)

    def uint32(self):
        t = rshift(127 & self.buffer[self.pos], 0)
        if self.buffer[self.pos] < 128:
            self.pos += 1
            return t
        self.pos += 1
        t = rshift(t | (127 & self.buffer[self.pos]) << 7, 0)
        if self.buffer[self.pos] < 128:
            self.pos += 1
            return t
        self.pos += 1
        t = rshift(t | (127 & self.buffer[self.pos]) << 14, 0)
        if self.buffer[self.pos] < 128:
            self.pos += 1
            return t
        self.pos += 1
        t = rshift(t | (127 & self.buffer[self.pos]) << 21, 0)
        if self.buffer[self.pos] < 128:
            self.pos += 1
            return t
        self.pos += 1
        t = rshift(t | (15 & self.buffer[self.pos]) << 28, 0)
        if self.buffer[self.pos] < 128:
            self.pos += 1
            return t
        self.pos += 1

    def int32(self):
        return 0 | self.uint32()

    def boolean(self):
        return 0 != self.uint32()

    def bytes(self):
        t = self.uint32()
        e = self.pos
        n = self.pos + t
        if n < len(self):
            self.pos += t
            return bytes(self.buffer[e: n])
        return b''

    def string(self):
        t = self.bytes()
        return t.decode('utf-8')

    def skip(self, n=None):
        if n is int:
            self.pos += n
        else:
            while (128 & self.buffer[self.pos]) > 0:
                self.pos += 1

    def skip_type(self, n):
        if n == 0:
            self.skip()
        elif n == 1:
            self.skip(8)
        elif n == 2:
            self.skip(self.uint32())
        elif n == 3:
            t = 7 & self.uint32()
            while t != 4:
                self.skip_type(t)
                t = 7 & self.uint32()
        elif n == 5:
            self.skip(4)


class MPObject:
    def __init__(self, buffer: MPData, t):
        n = buffer.pos + t
        if n <= len(buffer):
            while buffer.pos < n:
                a = rshift(buffer.uint32(), 3)
                self._decode(buffer, a)

    @abstractmethod
    def _decode(self, buffer: MPData, a):
        pass


def rshift(val, n):
    if val >= 0:
        return val >> n
    return (val + 0x100000000) >> n