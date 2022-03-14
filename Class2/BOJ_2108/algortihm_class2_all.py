#BOJ 2108 Silver3
from re import U


n = int(input())

num_list = []
for _ in range(n):
    k = int(input())
    num_list.append(k)

'''
class Stac:
    def __init__(self):
        self.list = num_list
    
    def mean(self):
        x = 0
        for i in range(len(self.list)):
            x  += self.list[i] 
        return print(int(round(x/len(self.list),0)))
    
    def median(self):
        self.list.sort()
        #홀수면 가운대
        #짝수면 앞뒤 중간
        #홀수
        a = len(self.list)//2 
        return print(self.list[a])

    
    def mode(self):
        self.list.sort()
        number = list(set(self.list))
        max_fre = []
        max_cnt = 0
        for i in number:
            if max_cnt == self.list.count(i):
                max_fre.append(i)
            elif max_cnt < self.list.count(i):
                max_fre = []
                max_fre.append(i)
                max_cnt = self.list.count(i)
        if len(max_fre) > 1:
            max_fre.sort()
            return print(max_fre[1])
        else:
            return print(max_fre[0])

    def diff(self):
        self.list.sort()
        return print(self.list[len(self.list)-1]- self.list[0])
        
        

stac = Stac()
stac.mean()
stac.median()
stac.mode()
stac.diff()
'''
x= 0
for i in range(len(num_list)):
    x  += num_list[i] 
print(int(round(x/len(num_list),0)))
num_list.sort()
        #홀수면 가운대
        #짝수면 앞뒤 중간
        #홀수
a = len(num_list)//2 
print(num_list[a])
highs = [num_list[0]]
cnt = 1
high = 0
last = num_list[0]
idx = 0
for i in num_list[1:]:
    if i != last:
        if cnt > high:
            highs = []
            highs.append(last)
            high = cnt
        elif cnt == high and last not in highs:
            highs.append(last)
        cnt = 1
    else:
        cnt +=1
    last = i
    idx += 1
if cnt > high:
    highs = [last]
elif cnt == high and last not in highs:
    highs.append(last)
cnt =1
if len(highs) == 1:
    print(highs[0])
else:
    print(highs[1])

print(num_list[len(num_list)-1]- num_list[0])