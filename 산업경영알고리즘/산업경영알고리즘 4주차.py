import random


#선택 정렬 함수 
def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = i
        for k in range(i+1,n):
            if (ary[minIdx]<ary[k]):  #내림차순
                minIdx = k
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp

    return ary

#랜덤리스트 생성 함수
def randomList(i):
    list = []
    while len(list) < i:          
        randNumber = random.randint(0,200)  
        if randNumber not in list:   
            list.append(randNumber)
    return list


dataAry = randomList(10)

print(f"정렬전 ---> {dataAry}")
dataAry = selectionSort(dataAry)
print(f"정렬후 ---> {dataAry}")
