import math
n,m = map(int,input().split())
lenn = len(str(n))
lenm = len(str(m))

#code thuoc so huu cua Dang Thanh Phat
#Hackerrank: dangthanhphat911
#Codeforces: alexei_pc

def countZeros(n):
    if n<=0: return 0
    result = 0
    i = 1

    while True:
        b, c = divmod(n, i)
        a, b = divmod(b, 10)

        if a == 0:
            return result

        if b == 0:
            result += (a - 1) * i + c + 1
        else:
            result += a * i

        i *= 10
        
if n-1>0 : res = countZeros(m)-countZeros(n-1)
elif n==0: res = countZeros(m)+1
else: res = countZeros(m)

print(res,'\n')
    
