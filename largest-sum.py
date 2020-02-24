import math

#code thuoc so huu cua Dang Thanh Phat
#Hackerrank: dangthanhphat911
#Codeforces: alexei_pc

#input
n = int(input())
x = input()
a = [int(i) for i in x.split()]
#solve
maxend = 0
res = -100000
for i in range(n):
    maxend = maxend+a[i]
    res = max(maxend,res)
    if maxend<0:
        maxend = 0
print(res,'\n')
