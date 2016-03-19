from random import getrandbits
# from base64 import b64encode as b64e, b64decode as b64d


class RandomBytes:
    def __init__(self):
        self.r = self._generate()

    def _generate(self):
        """r = timeit.timeit("'%0x' % getrandbits(30 * 4)",
                          "from random import getrandbits")
        return binascii.hexlify(bytes(str(r).split('.')[-1], 'utf-8'))"""
        # return out.encode('ascii')
        return hex(getrandbits(256))

    def __repr__(self):
        return str(self.r).split('0x')[-1]


if __name__ == '__main__':
    print(RandomBytes())
