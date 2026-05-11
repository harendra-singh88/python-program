class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        r=1
        if n<0:
            p=abs(n)
            for i in range(1,(p+1)):
                r=r/x

        else:
            for i in range(1,(n+1)):
                r=r*x
        print(r)
        return x
new2=Solution()
new2.myPow(2,10)