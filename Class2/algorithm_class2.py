#!/usr/bin/env python
# coding: utf-8

# In[1]:


progress = []
speeds = []
#answer = return

def solution(progresses, speeds):
    done = 0
    time = 0
    answer = []
    while len(progresses)>0:
        if progresses[0]+time*speeds[0] >=100:
            progresses.pop(0)
            speeds.pop(0)
            done +=1
        else:
            if done >0:
                answer.append(done)
                done =0
            time +=1
    answer.append(done)
    return answer

solution(progress, speeds)


# In[13]:


array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]


def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        a = commands[i][0]
        b = commands[i][1]
        c = commands[i][2]
        arr_list = array[a-1:b]
        arr_list.sort()
        answer.append(arr_list[c-1])
    return answer

    
solution(array, commands)


# In[31]:


a,b = map(int,input().split())
array = [0]


for i in range(b+1):
    for j in range(i):
        array.append(i)
print(len(array))
print(array)
print(sum(array[a:b+1]))


# In[34]:


'''
과목 개수 c 입력받으면
과목1 -> 점수 점수 점수
과목2 -> 점수 점수
과목c -> 점수 점수 점수 점수

count(mean(과목1) > 점수 in 과목1)/count(점수) -> 소수점 셋째자리

'''
c = int(input())
for i in range(c):
    case = list(map(int,input().split()))
    case_sum = sum(case[1:])
    mean = case_sum/(len(case)-1)
    value = [case[i]> mean for i in range(len(case))]
    value = value[1:]
    count = 0
    for j in range(len(value)):
        if value[j] == True:
            count += 1
    n = count/(len(case)-1)*100
    print("{:.3f}%".format(n))
    


# In[42]:


x,y,w,h = map(int,input().split())
len_list = [x,w-x,y,h-y]
print(min(len_list))


# In[71]:


n = int(input())
words = []
for i in range(n):
    word = str(input())
    words.append(word)
words = set(words)
words = list(words)
words.sort(key = lambda x: (len(x),x))

for word in words:
    print(word, end="\n")






# In[5]:



x = int(input())
check_list = set(map(int,input().split()))
num = int(input())
num_list = list(map(int,input().split()))

for num in num_list:
    if num in check_list:
        print(1,end="\n")
    else:
        print(0,end="\n")


# In[ ]:


check = int(input())
check_list = list(map(int, input().split(' ')))
check_list.sort()

num = int(input())
num_list = list(map(int, input().split(' ')))


def binary(target):
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if n_list[mid] == target:
            return True

        if target < n_list[mid]:
            right = mid-1
        elif target > n_list[mid]:
            left = mid + 1


for i in range(num):
    if binary(num_list[i]):
        print(1)
    else:
        print(0)


# In[13]:


n = int(input())
num_list = []
for i in range(n):
    num = tuple(map(int,input().split()))
    num_list.append(num)
num_list.sort()
for num in num_list:
    num = list(num)
    print(num[0], num[1])


# In[14]:


n = int(input())
num_list = []
for i in range(n):
    [x,y] = map(int,input().split())
    num_list.append([x,y])
num_list.sort()
for num in num_list:
    print(num[0], num[1])


# In[27]:


n = int(input())
ls = []
for i in range(n):
    [age,name] = input().split()
    ls.append([int(age),name])

ls.sort(key = lambda x: x[0])

for l in ls:
    print(l[0],l[1])


# In[41]:



import sys
n = int(input())  # sys.stdin.readline()
num_list = []
for i in range(n):
    num = int(input()) #sys.sydin.readline()
    num_list.append(num)
num_list = set(num_list)
num_list = list(num_list)
num_list.sort()
for i in range(len(num_list)):
    print(num_list[i])


# In[2]:


n,k= map(int,input().split())
num_list = [n+i for i in range(k-n+1)]

def sosu(num):
    if num == 1:
        return 0
    elif num ==2:
        return num;
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return 0;
    return num;

    
for i in num_list:
    if sosu(i) != 0:
        print(sosu(i))
                


# In[ ]:





# In[13]:


n = int(input())

for i in range(n):
    num = list(input())
    cnt = 0
    for j in num:
        if j == '(':
            cnt +=1;
        elif j == ')':
            cnt -=1;
        if cnt <0:
            print('NO')
            break;
    if cnt==0:
        print('YES')
    elif cnt >0:
        print('NO')


# In[12]:




n = int(input())
num_list = list(map(int,input().split()))

c = int(input())
check_list = list(map(int,input().split()))



exist = []
for check in check_list:
   if check in num_list:
       exist.append(check)
exist.sort()
def binary_search(num):
   left = 0
   right = len(exist)-1
   cnt = 0
   for i in range(len(exist)):
       mid = (left+right)//2
       if num == exist[mid]:
           return print(cnt)
       
       if num > exist[mid]:
           left = mid+1
           cnt+=1
       elif num < exist[mid]:
           right = mid-1
           cnt +=1
           
for num in num_list:
   binary_search(num)
   
   


# In[1]:


n = int(input())
num_list = list(map(int,input().split()))

c = int(input())
check_list = list(map(int,input().split()))

hash = {}

for num in num_list:
    if num in hash:
        hash[num] +=1
    else:
        hash[num] =1

for check in check_list:
    if check in hash:
        print(hash[check],end =" ")
    else:
        print(0,end=" ")


# In[ ]:




def binary_search(num):
    left = 0
    right = n-1
    cnt = 0
    for i in range(n):
        mid = (left+right)//2
        if num == num_list[mid]:
            return num
        
        if num > num_list[mid]:
            left = mid+1
        elif num < num_list[mid]:
            right = mid-1

a_list = []
for check in check_list:
    a_list.append(binary_search(check))

for a in a_list:
    if a in num_list:


# In[7]:

while True:
    num_list = list(map(int,input().split()))
    num_list.sort()
    a = num_list[0]
    b = num_list[1]
    c = num_list[2]
    if a**2 + b**2 == c**2 and c != 0:
        print('right')
        num_list = []
    elif a==0 and b==0 and c ==0:
        break;
    else:
        print('wrong')
        num_list = []


# In[18]:


n,k = map(int,input().split())

#n -> +1 , -1, *2 -> n=k

cnt = 0
num_list = []
for i in range(n,k+1):
    num_list.append(i)


# In[20]:


n,k = map(int,input().split()) # BFS를 위한 que 
que = [] # 방문 여부를 판단하기위한 que 
v_que = [ 0 for _ in range(100001)]# 방문한 곳의 depth를 기록하기 위한 que 
depth = [] # 출발위치 입력. 
depth.append(0) 
que.append(n) 
while True: # 현재위치와 depth 
    x = que.pop(0) 
    xc = depth.pop(0) # 방문하지 않았던 곳이면 실행. 
    if v_que[x] != 1 : 
        v_que[x] = 1 # 총 3가지 이동옵션이 있음 # 조건을 만족할시 이동 수행. 
        if x-1 >= 0: 
            que.append(x-1) # 현재 depth + 1 
            depth.append(xc + 1) 
        if 2*x <= 100000 : 
            que.append(2*x) 
            depth.append(xc + 1) 
        if x+1 <= 100000 : 
            que.append(x+1) 
            depth.append(xc + 1) 
    if x == k: 
        print(xc) 
        break


# In[32]:


num = int(input())
num_list = list(map(int,input().split()))
s = 0
for k in num_list:
     s += k
num = s/num
result = num/max(num_list)*100
print(result)


# In[44]:


n,k = map(int,input().split())
for i in range(min(n,k),0,-1):
    if n%i ==0 and k%i ==0:
        print(i)
        break;
for i in range(max(n,k),(n*k)+1):
    if i%n==0 and i%k==0:
        print(i)
        break
        


# In[45]:


import math
n,k = map(int,input().split())
print(math.gcd(n,k))
print(math.lcm(n,k))

In[58]:


n,k = list(map(str,input().split()))
for i in range(len(n)):
    if i ==0:
        re
    result += result[-i]


In[32]:


n,k = map(int,input().split())
box_list =[]
for i in range(k):
    num = list(map(int,input().split()))
    box_list.append(num)

while True:
    if box_list[0][0]


In[ ]:


#백준 7576 토마토
from collections import deque
m,n = map(int,input().split())
matrix = [list(map(int,input().split())) for i in range(n)]
queue = deque() #bfs -> queue -> pop(0) : O(n), deque -> popleft() : O(1)
#방향리스트
dx = [-1,1,0,0]
dy = [0,0,-1,1] 
# dx:1 dy:0 ->  왼쪽 , dx:0, dy: -1 -> 아래
# 만약 대각선 추가한다면 dx: [-1,1,0,0,-1,-1,1,1] , dy=[0,0,-1,1,-1,1,-1,1]

res= 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] ==1:
            queue.append([i,j])

#bfs -> 한번 들어가면 다 돌아서 재귀할 필요 X

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):  #왼오아래위
            nx, ny = dx[i]+x, dy[i] + y
            if 0<=nx < n and 0 <= ny < m and matrix[nx][ny] ==0: #범위안에 들어오면 and 1일대
                matrix[nx][ny] = matrix[x][y] +1  # 카운트업 1->2->3 -> 4->5 ->6  ... 마지막 -1 : 총 카운트
                queue.append([nx,ny]) # 다시 queue에 넣어져서 반복하기
bfs()
for row in matrix:
    for col in row:
        # 다 찾아봤는데 토마토를 익히지 못했다면 -1 출력
        if col == 0:
            print(-1)
            exit(0)
    # 다 익혔다면 최댓값이 정답
    res = max(res,max(row))
# 처음 시작을 1로 표현했으니 1을 빼준다.
print(res - 1)      
    


In[ ]:


from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque()

    # 시작노드 큐에 담기
    queue.append(start)

    # 방문 노드와 연결된 모든 노드들을 담고 하나씩 방문
    while queue:
        # 큐의 맨 앞 노드 빼오기
        now = queue.popleft()
        # 아직 방문하지 않았다면 방문 마크 후 인접 노드들 큐에 넣기
        if now not in visited:
            visited.append(now)
            queue.extend(graph[now])

    return ' '.join(visited)

graph = {
    'A': ['B'],
    'B': ['A', 'H', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

print(bfs(graph, 'A'))


In[3]:


from collections import deque

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(matrix,a,b):
    queue = deque()
    queue.append([a,b])
    matrix[a][b] = 0
    
    while queue:
        x,y = queue.popleft()
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            
            if 0<=nx<N and 0<=ny <M:
                if matrix[nx][ny] ==1:
                    matrix[nx][ny] =0
                    queue.append([nx,ny])
            
T = int(input())
for t in range(T):
    N,M,K = map(int,input().split())
    matrix = [[0]*M for _ in range(N)]
    for _ in range(K):
        a,b = map(int,input().split())
        matrix[a][b] =1
    
    cnt = 0
    for row in range(N):
        for col in range(M):
            if matrix[row][col] ==1:
                bfs(matrix,row,col)
                cnt +=1
    print(cnt)
    


In[9]:


from collections import deque
n = int(input())
k = int(input())
num_list = [list(map(int,input().split())) for _ in range(k)]
graph = {}
for num in num_list:
    graph[num[0]] = graph.get(num[0],[]) + [num[1]]
    graph[num[1]] = graph.get(num[1],[]) + [num[0]]
queue = deque()
visited = []
def bfs():
    queue.append(1)
    visited.append(1)
    while queue:
        x = queue.popleft()
        if x == 1:
            queue.append(graph[1])
            for num in graph[1]:
                visited.append(num)
        else:
            for i in x:
                for num in graph[i]:
                    if num not in visited:
                        queue.append(graph[i])
                        visited.append(num)
bfs()
print(len(visited)-1)


In[11]:


num1, num2 = map(str,input().split())
num1 =int(num1[::-1])
num2 =int(num2[::-1])
if num1>num2:
    print(num1)
else:
    print(num1)


#In[1]:


T = int(input())
for _ in range(T):
    x,y = input().split()
    for word in y:
        print(int(x)*word, end="")
    print()


 In[ ]:


T = int(input())
num_list = [map(int,input().split()) for _ in range(T)]
            


 In[11]:


import sys
K, N = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(lan) 

while start <= end: #적절한 랜선의 길이를 찾는 알고리즘
    mid = (start + end) // 2 #중간 위치
    lines = 0 #랜선 수
    for i in lan:
        lines += i // mid #분할 된 랜선 수
        
    if lines >= N: #랜선의 개수가 분기점
        start = mid + 1
    else:
        end = mid - 1
print(end)



In[ ]:







