# program for reverse the number 

class Solution(object):
    def reverse(self, x):
        sign= -1 if x<0 else 1
        num1=abs(x)
        print("good morning")
        reverse_num=0
        while num1>0:
            num=x%10
            reverse_num=reverse_num*10+num # type: ignore
            x//=10
        # return reverse_num*sign
        print(reverse_num*sign)
solu1=Solution()
solu1.reverse(345)
