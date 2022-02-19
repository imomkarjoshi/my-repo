class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, n, r, p):

        num = den = 1
        for i in range(r):
            num = (num * (n - i)) % p
            den = (den * (i + 1)) % p
        return (num * pow(den, p - 2, p)) % p


A = 41
B = 27
C = 143

print(Solution().solve(A, B, C))
