#fibonachi
import sys

T = int(sys.stdin.readline())
cnt1 =[1,0]
cnt2 =[0,1]

for _ in range(T):
    N = int(sys.stdin.readline())
    
    if N == 0:
        print(cnt1[0], cnt1[1])
    elif N == 1:
        print(cnt2[0], cnt2[1])    
    else:
        for i in range(2,N+1):
            cnt1.append(cnt1[i-1]+cnt1[i-2])
            cnt2.append(cnt2[i-1]+cnt2[i-2])
        print(cnt1.pop(), cnt2.pop())
        cnt1 =[1,0]
        cnt2 =[0,1]           

