class Solution(object):
   
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            print(False)
        original_num=x
        revers_num=0
        while x>0:
            digit=x%10
            revers_num=revers_num*10+digit
            x//=10
            # return original_num==revers_num
        if original_num ==revers_num:
            print(True)
        else:
            print(False)
solu=Solution()
solu.isPalindrome(454)           
