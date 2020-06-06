class Solution(object):


    #求两数和
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xFFFFFFFF
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        if a >> 31 == 0:
            return a
        else:
            return a - 2 ** 32

    #求二进制中'1'的个数(负数用补码表示）
    def NumberOf1(self, n):
        cnt = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            n = n & (n - 1)
            cnt += 1
        return cnt
    #把一个数的二进制进行翻转 Reverse bits of a given 32 bits unsigned integer.
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans


if __name__=="__main__":
    S=Solution()
    n=2
    print(S.NumberOf1(n))
