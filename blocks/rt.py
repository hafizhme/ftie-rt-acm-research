class RT:
    def __init__(self, bbs):
        """
        INPUT
        bbs         blocks.bbs.BBS
        """
        self.__bbs = bbs

    def encrypt(self, plaintext):
        """
        INPUT
        plaintext   [int 0...N-1]
        OUTPUT
        ciphertext   [int 0...2N-2]
        """
        from random import randint
        ciphertext = []
        for _p in plaintext:
            random = randint(0, 256)
            key = self.__bbs.next()
            ciphertext.append(
                (key + 2 * _p + random) % 256
            )
            ciphertext.append(
                (2 * key + _p + random) % 256
            )

        return ciphertext

    def decrypt(self, ciphertext):
        """
        INPUT
        ciphertext   [int 0...2N-2]
        OUTPUT
        plaintext   [int 0...N-1]
        """
        plaintext = []
        for i in range(int(len(ciphertext) / 2)):
            key = self.__bbs.next()
            plaintext.append(
                (ciphertext[2 * i] - ciphertext[2 * i + 1] + key) % 256
            )

        return plaintext
