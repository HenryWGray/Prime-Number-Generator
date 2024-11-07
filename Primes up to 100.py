import time
start=time.time()
print("Starting...")
# Method 1 for finding primes
import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "primePy"])
from primePy import primes
primes=(primes.upto(100000))
print("it's really as shrimple as that")




# # Method 2 for finding primes

# x=3
# oTH=[]
# nP=[]
# p=[]
# oT=[2]
# while(x<100000):
#     v=2
#     while(v<100000):
#         if(v*x>100000):
#             v=100000
#             break
#         nP.append(v*x)
#         v=v+1
#     oTH.append(x)
#     x=x+2
    
# lst3 = [value for value in oTH if value not in nP]
# primes=(oT+lst3)

# # Method 3 for primes. Method provided by Eli.
# print("Calculating primes...")
# x=3
# primes=[2]
# while(x<100000):
#     prime=True
#     for i in primes:
#         if(i>x/2):
#             break
#         if(x%i==0):
#             prime=False
#     if prime==True:
#         primes.append(x)
#     x=x+1

# # Primary method for discovering lowest difference between sets of primes

# n=0
# v=10000
# wh=[]
# while(n<len(primes)-10):
#     t=n+10
#     if(primes[t]-primes[n]<v):
#         v=primes[n+10]-primes[n]
#         wh=[n,n+10]
#     n=n+1

# print(f"At a distance of {v} from one another, the two closes primes can be found at indexes {wh[0]} and {wh[1]}. \nThe primes are {primes[int(wh[0])]} and {primes[int(wh[1])]}")

# Stemming from a better idea of what is being asked,
print("Calculating distance...")
n=0
sL=[100,100,100,100,100,100,100,100,100,100]
iX=[0,0,0,0,0,0,0,0,0,0]
while(n<len(primes)-1):
    if primes[n+1]-primes[n] < max(sL):
        iX[sL.index(max(sL))]=(primes[n],primes[n+1])
        sL[sL.index(max(sL))]=primes[n+1]-primes[n]
    n=n+1
print(iX,sL)


end=time.time()
print(f"Runtime is {(end-start)*(10**3)} ms")