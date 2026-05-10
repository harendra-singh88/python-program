n=int(input("enter the number"))
def factorail(n):
    if n==0  or n==1:
        return 1
    else :
        return n*factorail(n-1)
a=factorail(n)
print("factorail of 5 is ",a)